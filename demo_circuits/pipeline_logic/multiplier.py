from docopt import docopt
import time
import pprint
from seal.prs import pipeline_logic as logic
from seal import tracem as tr
from seal import plotting
from seal import preprocessing as p


usage_msg = """

TODO
Explain what the script does
cutoff


usage:
    multiplier.py [options]

Options:
-h --help                   Show this screen.
-v --version                Show version information.

--runtime=T                 Time for execution prefix.
                            [default: 400].    
--golden                    Golden run.
--snk=D                     Sink delay.
                            [default: 0].
--src=D                     Source delay.
                            [default: 0].
--fault=F                   Fault type to check (possible values: SA0, SA1, SAF)
                            [default: SAF].               
--testcase                  Check a specific fault injection.
--delta2                    Check using checkdelta2.
--deltaopt                  Check using checkdeltaopt.
--cutoff-min=N              The minimal cutoff. the start of the window to investigate
                            [default: 0].
--cutoff-max=N              The maximal cutoff. the end of the window to investigate
                            [default: float('Inf')].               
"""
#--------|---------|---------|---------|---------|---------|---------|---------|

def main():
    options = docopt(usage_msg, version="0.1")    

#--------|---------|---------|---------|---------|
    if (options["--delta2"]):
        from seal import checkdelta2 as check
    elif(options["--deltaopt"]):
        from seal import checkdeltaopt as check
    else:
        from seal import checkdelta as check
#--------|---------|---------|---------|---------|
    if (options["--golden"]):
        golden = True
    else:
        golden = False

    T = int(options["--runtime"])
    snk = int(options["--snk"])
    src = int(options["--src"])
    fault = str(options["--fault"])
    assert (fault in ['SAF', 'SA1', 'SA0']), "Fault type not supported"

    if (options["--testcase"]):
        CHECK = False
    else:
        CHECK = True

    cutoff_min = int(options["--cutoff-min"])
    cutoff_max = float(options["--cutoff-min"])

    # create circuit
    init, events, tokens, input_widths, output_signals, output_widths = logic.umul4x4_new.GeneratePipeline()
    
    if not CHECK:
        if fault == 'SA1':
            stuck_sig = 'a(3).F'
            stuck_val = 1
            stuck_t = 300
            events += [
                    (stuck_t, stuck_sig, stuck_val),  # add SA1 
            ]

            # checking that it will stay stuck
            # events += [(stuck_t, stuck_sig, not stuck_val)]
            # events += [(stuck_t+10, stuck_sig, not stuck_val)]

            times, states = tr.traceSA(init, events, output_signals, stuck_sig, stuck_val, stuck_t, T=T, monitor=True, tokens=tokens, input_widths=input_widths, output_widths=output_widths)
            # times, states = tr.trace(init, events, output_signals, T=T, monitor=True, tokens=tokens, input_widths=input_widths, output_widths=output_widths)
        
        elif fault == 'SA0':
            stuck_sig = 'op(0).F'
            stuck_val = 0
            stuck_t = 83.2645698969215
            events += [  
                    (stuck_t, stuck_sig, 0),  # add SA0
            ]

            # checking that it will stay stuck
            # events += [(stuck_t, stuck_sig, not stuck_val)]
            # events += [(stuck_t+10, stuck_sig, not stuck_val)]

            times, states = tr.traceSA(init, events, output_signals, stuck_sig, stuck_val, stuck_t, T=T, monitor=True, tokens=tokens, input_widths=input_widths, output_widths=output_widths)

        else:
            raise Exception("SAF can only be combined with CHECK")
        
    # if CHECK, run golden run without any faults
    else:
        times, states = tr.trace(init, events, output_signals, T=T, snk_delay=snk, src_delay=src, monitor=True, tokens=tokens, input_widths=input_widths, output_widths=output_widths)
        # print("print after trace call", events)

    plotting.plot(times, states, list(init.keys()))
    # print(events)

    if not golden:
        if CHECK:
            start = time.time()

            SA1_M = {}
            SA0_M = {}

            if fault == 'SAF' or fault == 'SA1':
                SA1_M = check.checkSA(
                    times=times,
                    states=states,
                    events=events,
                    signals=list(init.keys()),
                    output_signals=list(output_signals),
                    snk_delay=snk,
                    src_delay=src,
                    cutoff_min=cutoff_min,
                    cutoff_max=cutoff_max,
                    fault='SA1',
                    monitor=True,
                    tokens=tokens,
                    input_widths=input_widths,
                    output_widths=output_widths,
                    # victim_signals=[]
                    victim_signals=['ack_in']
                )
                # pprint.pprint(SA1_M)

            if fault == 'SAF' or fault == 'SA0':
                SA0_M = check.checkSA(
                    times=times,
                    states=states,
                    events=events,
                    signals=list(init.keys()),
                    output_signals=list(output_signals), 
                    cutoff_min=cutoff_min,
                    cutoff_max=cutoff_max,
                    fault='SA0',
                    monitor=True,
                    tokens=tokens,
                    input_widths=input_widths,
                    output_widths=output_widths,
                    # victim_signals=[]
                    victim_signals=['ack_in']
                )
                # pprint.pprint(SA0_M)

            end = time.time()

            susceptible_SA1 = p.appendSAF(p.collapseRanges(SA1_M['susceptible'] if SA1_M else []), 'SA1')
            susceptible_SA0 = p.appendSAF(p.collapseRanges(SA0_M['susceptible']if SA0_M else []), 'SA0')
            print(f"Susceptible SA1: {susceptible_SA1}")
            print(f"Susceptible SA0: {susceptible_SA0}")

            susceptible = susceptible_SA1 + susceptible_SA0

            total_time = end - start
            print(f"\n time to check circuit using checkdelta is {total_time}")

            plotting.plot(
                times,
                states,
                list(init.keys()),
                susceptible=susceptible,
                fault=fault,
                cutoff=[cutoff_min, cutoff_max],
                fname="multiplier.svg"
                )

if (__name__ == "__main__"):
    main()

