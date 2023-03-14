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
    # print(tfrom, tto)

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
        middle = (tto + tfrom)/2

        if tto - tfrom <= 0.05:
            return middle

        else:
            middle_is_M = isSusceptible(t=middle, s=s, states=states, s_state=s_state, events=events, T=T, output_signals=output_signals, MafterGrid=0.001)

            if middle_is_M:
                # boundary must be on the left half
                return findBoundary(tfrom=tfrom, tto=middle, s=s, states=states, s_state=s_state, events=events, T=T, output_signals=output_signals, initially=False)
            else:
                # boundary must be on the right half
                return findBoundary(tfrom=middle, tto=tto, s=s, states=states, s_state=s_state, events=events, T=T, output_signals=output_signals, initially=False)




def check(times, states, events, signals, output_signals,
    Textra=30,
    exclude_output_signals=True,
    cutoff_min=0, cutoff_max=float('Inf')):
    """
    checking all equivalence regions
    """
    susceptible_intervals = []
    pos = 0
    neg = 0
    pos_per_sig = { s: 0 for s in signals }
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
            
            assert (tto - boundary >= 0)
            assert (boundary - tfrom >= 0)

            pos += tto - boundary
            neg += boundary - tfrom

            pos_per_sig[s] += tto - boundary

    for s in output_signals:
        pos_per_sig[s] += times[-1] - times[0]

        if not exclude_output_signals:
            susceptible_intervals += [ (s, [times[0], times[-1]]) ]
            pos += times[-1] - times[0]

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
        'p_per_sig': { s: pos_per_sig[s] / (times[-1] - times[0]) for s in signals },
        'cutoff_min': cutoff_min,
        'cutoff_max': cutoff_max,
        'susceptible': susceptible_intervals
    }
