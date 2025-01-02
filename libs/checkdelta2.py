from tqdm import tqdm

from libs import tracem as tr

ERROR = 1e-6
error_cause=False

def isSusceptibleSA(t, s, states, events, T, output_signals, SAF, MafterGrid,	#	MafterGrid=0.001
                    snk_delay=10, src_delay=10,
                    monitor=False, tokens=None, input_widths=None, output_widths=None): 
        
    events_check = events + [
        (t + MafterGrid, s, SAF),           # add SA0 or SA1
    ]
    times_M, states_M = tr.traceSA(states[0], events_check, output_signals, SA_signal=s, SA_value=SAF, SA_time=t+MafterGrid,
                                T=T, snk_delay=snk_delay, src_delay=src_delay,
                                monitor=monitor, tokens=tokens, input_widths=input_widths, output_widths=output_widths, verbose=False) #	Mdelay=t+MafterGrid,
    
    was_M = False
    for state_M in states_M:
        was_M = was_M or any([ state_M[s] == 0.5 for s in output_signals ])	

    # print((f"SA_signal {s} stuck at {SAF} at time {t+MafterGrid} {was_M}"))
    return was_M
                

def findDelta(signal: str, time: float, times: list[float]) -> float:
    """
    By how much we can proceed.
    """
    # print(f"signal {signal} at time {time}")
    times_larger = [t for t in times if t > time]
    if len(times_larger) == 0:
        return float("inf")

    end_of_region = min(times_larger)
    duration_on_own_signal = end_of_region - time

    ret = [ duration_on_own_signal ]
    outputList = tr.getOutputList(signal)
    for output in outputList:
        out_sig = output[0]
        delay = output[1]
        delta =findDelta(out_sig, time + delay, times)
        assert delta>0

        # ret += [ findDelta(out_sig, time + delay, times) ]
        ret += [delta]
    return min(ret)


def checkSA(times, states, events, signals, output_signals,
    snk_delay=10, src_delay=10,
    Textra=30,
    exclude_output_signals=True,
    cutoff_min=0, cutoff_max=float('Inf'),
    fault='SA0',
    monitor=False,
    tokens=None,
    input_widths=None,
    output_widths=None,
    victim_signals=[]
    ):

    """
    checking all equivalence regions
    """
    susceptible_intervals = []
    pos = 0
    neg = 0
    pos_per_sig = { s: 0 for s in signals }
    T = times[-1] + Textra

    if fault == 'SA0':
        SAF = 0
    elif fault == 'SA1':
        SAF = 1

    non_output_signals = [ s for s in signals if s not in output_signals ]

    if monitor:
        if tokens is None or input_widths is None or output_widths is None:
            raise Exception("Tokens and In/Output Widths missing!")

    # go over regions
    count=0
    if victim_signals:
        # to test only a set of signals
        victims = tqdm(victim_signals, leave=True, desc=f"Victim Signals Progress for {fault}")
    else:
        # testing all signals
        victims = tqdm(non_output_signals, leave=True, desc=f"Victim Signals Progress for {fault}")

    for s in victims:
        count+=1

        for i in range(len(times)-1):
            tfrom = times[i]
            tto = times[i+1]

            while True:
                # step 1: find the smallest delta
                delta = findDelta(s, tfrom, times)
                mid_point = delta/2 + tfrom

                # step 2: inject a fault anywhere within delta
                region_is_M = isSusceptibleSA(t=mid_point, s=s, states=states, events=events, T=T, output_signals=output_signals, SAF=SAF, MafterGrid=ERROR,
                               snk_delay=snk_delay, src_delay=src_delay,
                               monitor=monitor, tokens=tokens, input_widths=input_widths, output_widths=output_widths)

                # step 3: label the delta region (and add to pos & neg & pos_per_sig[s] accordingly)
                if region_is_M:
                    susceptible_intervals += [ (s, [tfrom, tfrom+delta]) ]
                    pos += delta - tfrom
                    pos_per_sig[s] += delta - tfrom
                else:
                    neg += delta - tfrom

                tfrom += delta

                if tfrom >= tto:
                    break

    for s in output_signals:
        pos_per_sig[s] += times[-1] - times[0]

        if not exclude_output_signals:
            susceptible_intervals += [ (s, [times[0], times[-1]]) ]
            pos += times[-1] - times[0]


    p = pos/(pos+neg) if pos + neg > 0 else 'undefined'
    if victim_signals:
        p_per_sig = { s: pos_per_sig[s] / (times[-1] - times[0]) for s in victims }
    else:
        p_per_sig = { s: pos_per_sig[s] / (times[-1] - times[0]) for s in signals }

    # assert (p <= 1)
    # assert (p_per_sig[s] <= 1 for s in signals)

    return {
        'p': p,
        'p_per_sig': p_per_sig,
        'cutoff_min': cutoff_min,
        'cutoff_max': cutoff_max,
        'susceptible': susceptible_intervals
    }