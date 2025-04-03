import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
sys.path.append(dir_path + '/../')

import numpy as np

from libs import tracem as tr

def getStateAtTime(times, states, time: float):
    """
    given the execution as <times> and <states>,
    returns the state vector at time <time>
    """
    assert (time >= 0 and time <= times[-1]), "getStateAtTime: out of bounds time"

    for i, t in enumerate(times):
        if t > time:
            return states[i-1]

    return states[-1]


def check(times, states, events, signals, output_signals,
    Mdelta=0.01,
    Textra=30,
    MafterGrid=0.01,
    cutoff_min=0, cutoff_max=float('Inf')):
    """
    checking all equivalence regions
    """
    susceptible_intervals = []
    pos = 0
    neg = 0
    T = times[-1] + Textra

    non_output_signals = [ s for s in signals if s not in output_signals ]

    # construct regions backwards
    times_extra, states_extra = tr.trace(states[0], events=events, T=T, verbose=False)
    delays = tr.getDelays()
    print(delays)

    times_grid = set()
    times_grid_toprocess = set(times_extra + [ times[-1] ])  # dont forget the times[-1] line at the end umntil where to check

    current_time = max(times_grid_toprocess)
    while current_time >= 0:

        # work backwards with delays
        for delay in delays:
            times_grid_toprocess.add( current_time - delay ) 

        # add to grid
        times_grid.add( current_time )
        times_grid_toprocess.remove( current_time )

        # and go to next one
        current_time = max(times_grid_toprocess)
        # print(current_time)

    # remove duplicates and sort
    times_grid = sorted(list(times_grid))

    # remove all times that are > times[-1] -> only insert faults into these regions
    times_grid = [ t for t in times_grid if t <= times[-1] ]
    print(f'the time grid with the regions : {times_grid}')

    # construct the states for it
    states_grid = []
    for t in times_grid:
        states_grid += [ getStateAtTime(times=times, states=states, time=t) ]

    # go over regions
    for s in non_output_signals:
        for i in range(len(times_grid)-1):
            t = times_grid[i]
            events_check = events + [
                (t + MafterGrid,          s, 0.5),                # add glitch
                (t + MafterGrid + Mdelta, s, states_grid[i][s]),  # reset glitch
            ]
            times_M, states_M = tr.trace(states_grid[0], events=events_check, T=T, verbose=False)
            
            was_M = False
            for state_M in states_M:
                was_M = was_M or any([ state_M[s] == 0.5 for s in output_signals ])
            
            if times_grid[i] <= cutoff_max and times_grid[i+1] >= cutoff_min:
                ## region overlaps with cropped region
                t_from = max(cutoff_min, times_grid[i])
                t_to =   min(cutoff_max, times_grid[i+1])

                if was_M:
                    susceptible_intervals += [ (s, [t_from, t_to]) ]
                    pos += t_to - t_from
                else:
                    neg += t_to - t_from

    return {
        'p': pos/(pos+neg) if pos + neg > 0 else 'undefined',
        'cutoff_min': cutoff_min,
        'cutoff_max': cutoff_max,
        'susceptible': susceptible_intervals
    }
