from docopt import docopt
import time
from seal.prs import pipeline_logic as logic
from seal import tracem as tr
from seal import plotting
from seal import preprocessing as p


usage_msg = """

TODO
Explain what the script does
cutoff


usage:
    alu.py [options]

Options:
-h --help                   Show this screen.
-v --version                Show version information.

--runtime=T                 Time for execution prefix.
                            [default: 400].                   
-c --check                  Check all sensitivty windows.
--exhaustive                Check by injecting faults exhaustively (depricated version of check for SET).
--fault=F                   Fault type to check (possible values: SET, SA0, SA1, SAF)
                            [default: SAF].
--cutoff-min=N              The minimal cutoff. the start of the window to investigate
                            [default: 0].
--cutoff-max=N              The maximal cutoff. the end of the window to investigate
                            [default: float('Inf')].               
--delta2                    Check using checkdelta2.
"""
#--------|---------|---------|---------|---------|---------|---------|---------|

def main():
    options = docopt(usage_msg, version="0.1")

    # CHECK = True --> show sensitivity windows
    # CHECK = False --> show effect of specific glitches
    if (options["--check"]):
        CHECK = True
    else:
        CHECK = False
    CHECK = True

#--------|---------|---------|---------|---------|
    if (options["--exhaustive"]):
        from depricated import check
    elif (options["--delta2"]):
        from seal import checkdelta2 as check
    else:
        from seal import checkdelta as check
#--------|---------|---------|---------|---------|

    T = int(options["--runtime"])
    fault = str(options["--fault"])
    assert (fault in ['SET', 'SAF', 'SA1', 'SA0']), "Fault type not supported"

    cutoff_min = int(options["--cutoff-min"])
    cutoff_max = float(options["--cutoff-min"])

    # create circuit
    init, events, tokens, input_widths, output_signals, output_widths = logic.alu.GeneratePipeline()
    
    if not CHECK:
        if fault == 'SET':
            glitch_t = 29.521037528996843
            glitch_sig = 'd1__chin_op.T'
            events += [
                    (glitch_t, glitch_sig, 0.5),  # add glitch
                    (glitch_t + 0.1, glitch_sig, 0),  # reset glitch
            ]

            # print("print before trace call", events)
            times, states = tr.trace(init, events, output_signals, T=T, monitor=True, tokens=tokens, input_widths=input_widths, output_widths=output_widths)
            # print("print after trace call", events)

        elif fault == 'SA1':
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
        times, states = tr.trace(init, events, output_signals, T=T, monitor=True, tokens=tokens, input_widths=input_widths, output_widths=output_widths)
        # print("print after trace call", events)

    plotting.plot(times, states, list(init.keys()))
    # print(events)

    # # print it
    # for i in range(len(times)):
    #     print()
    #     print(f'time {times[i]}:')
    #     pprint.pprint(states[i])

    if CHECK:
        # if fault == 'SET':
        #     ret = check.check(
        #             times=times,
        #             states=states,
        #             events=events,
        #             signals=list(init.keys()),
        #             output_signals=output_signals,
        #             cutoff_min=cutoff_min,
        #             cutoff_max=cutoff_max,
        #             monitor=True,
        #             tokens=tokens,
        #             input_widths=input_widths,
        #             output_widths=output_widths,
        #             victim_signals=['op(0).F']   # 'd1__chin_op.T', 'b1__c_b_out_0'
        #     )
        #     pprint.pprint(ret)

        #     plotting.plot(
        #             times,
        #             states,
        #             list(init.keys()),
        #             susceptible=ret['susceptible'],
        #             cutoff=[cutoff_min, cutoff_max],
        #             )
        # else:
        start = time.time()
        SA1_M = {}
        SA0_M = {}

        if fault == 'SAF' or fault == 'SA1':
            SA1_M = check.checkSA(
                times=times,
                states=states,
                events=events,
                signals=list(init.keys()),
                output_signals=output_signals, 
                cutoff_min=cutoff_min,
                cutoff_max=cutoff_max,
                fault='SA1',
                monitor=True,
                tokens=tokens,
                input_widths=input_widths,
                output_widths=output_widths,
                # victim_signals=[]
                victim_signals=['op(0).F']
            )
            # pprint.pprint(SA1_M)

        if fault == 'SAF' or fault == 'SA0':
            SA0_M = check.checkSA(
                times=times,
                states=states,
                events=events,
                signals=list(init.keys()),
                output_signals=output_signals, 
                cutoff_min=cutoff_min,
                cutoff_max=cutoff_max,
                fault='SA0',
                monitor=True,
                tokens=tokens,
                input_widths=input_widths,
                output_widths=output_widths,
                victim_signals=[]
                # victim_signals=['op(0).F']
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
            )

if (__name__ == "__main__"):
    main()

