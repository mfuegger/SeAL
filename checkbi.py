import tracem as tr


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


def isSusceptible(t, s, states, s_state, events, T, output_signals, MafterGrid=0.001, Mdelta=0.001):
    events_check = events + [
        (t + MafterGrid,          s, 0.5),      # add glitch
        (t + MafterGrid + Mdelta, s, s_state),  # reset glitch
    ]
    times_M, states_M = tr.trace(states[0], events=events_check, T=T, verbose=False)
            
    was_M = False
    for state_M in states_M:
        was_M = was_M or any([ state_M[s] == 0.5 for s in output_signals ])

    return was_M


def findBoundary(tfrom, tto, s, states, s_state, events, T, output_signals, initially=True):
    # check if anywhere marked
    if not isSusceptible(t=tto, s=s, states=states, s_state=s_state, events=events, T=T, output_signals=output_signals, MafterGrid=-0.05):
        # no -> return boundary at end
        return tto

    # check if all marked (only initially)
    elif initially and isSusceptible(t=tfrom, s=s, states=states, s_state=s_state, events=events, T=T, output_signals=output_signals, MafterGrid=0.001):
        # yes -> return boundary at start
        return tfrom

    # else intersect
    else:
        if tto - tfrom <= 0.1:
            return (tto + tfrom)/2
        else:
            return findBoundary(tfrom=tfrom, tto=tto/2, s=s, states=states, s_state=s_state, events=events, T=T, output_signals=output_signals, initially=False)




def check(times, states, events, signals, output_signals,
    Textra=30,
    cutoff_min=0, cutoff_max=float('Inf')):
    """
    checking all equivalence regions
    """
    susceptible_intervals = []
    pos = 0
    neg = 0
    T = times[-1] + Textra

    non_output_signals = [ s for s in signals if s not in output_signals ]

    # go over regions
    for s in non_output_signals:
        for i in range(len(times)-1):
            tfrom = times[i]
            tto = times[i+1]
            boundary = findBoundary(tfrom=tfrom, tto=tto, s=s, states=states, s_state=states[i][s], events=events, T=T, output_signals=output_signals)

            if boundary < tto:
                # it has a marked area:
                susceptible_intervals += [ (s, [boundary, tto]) ]
            
            pos += tto - boundary
            neg += boundary - tfrom


            # if times[i] <= cutoff_max and times[i+1] >= cutoff_min:
            #     # region overlaps with cropped region
            #     t_from = max(cutoff_min, times[i])
            #     t_to =   min(cutoff_max, times[i+1])

            #     if was_M:
            #         susceptible_intervals += [ (s, [t_from, t_to]) ]
            #         pos += t_to - t_from
            #     else:
            #         neg += t_to - t_from

    return {
        'p': pos/(pos+neg) if pos + neg > 0 else 'undefined',
        'cutoff_min': cutoff_min,
        'cutoff_max': cutoff_max,
        'susceptible': susceptible_intervals
    }
