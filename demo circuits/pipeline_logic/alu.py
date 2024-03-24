from docopt import docopt
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../../')

import pprint
# from prs import linear_1Bit_3Stages as 
from prs import pipeline_logic as logic
from libs import tracem as tr
from libs import plotting
# from libs import checkbi as check
# from depricated import check

    # alu.py [-c | --check]
    # alu.py -h | -v

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
                            [default: 50].                   
-c --check                  Check all sensitivty windows.
--exhaustive                Check by injecting faults exhaustively (depricated version of check for SET).
--fault=F                   Fault type to check (possible values: SET, SA0, SA1)
                            [default: SET].
--cutoff-min=N              The minimal cutoff. the start of the window to investigate
                            [default: 0].
--cutoff-max=N              The maximal cutoff. the end of the window to investigate
                            [default: float('Inf')].               
"""
#--------|---------|---------|---------|---------|---------|---------|---------|

def main():
    options = docopt(usage_msg, version="0.1")

    # CHECK = True --> show sensitivity windows
    # CHECK = False --> show effect of specific glitches
    # if (options["--check"]):
    #     CHECK = True
    # else:
    #     CHECK = False
    CHECK = True

#--------|---------|---------|---------|---------|
    if (options["--exhaustive"]):
        from depricated import check
    else:
        from libs import checkbi as check
#--------|---------|---------|---------|---------|

    fault = str(options["--fault"])
    T = int(options["--runtime"])

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
            stuck_t = 9
            events += [
                    (stuck_t, stuck_sig, stuck_val),  # add SA1 
            ]

            # checking that it will stay stuck
            events += [(stuck_t, stuck_sig, not stuck_val)]
            events += [(stuck_t+10, stuck_sig, not stuck_val)]

            times, states = tr.traceSA(init, events, output_signals, stuck_sig, stuck_val, stuck_t, T=T, monitor=True, tokens=tokens, input_widths=input_widths, output_widths=output_widths)

        else:
            stuck_sig = 'a(0).T'
            stuck_val = 0
            stuck_t = 15
            events += [  
                    (stuck_t, stuck_sig, 0),  # add SA0
            ]

            # checking that it will stay stuck
            events += [(stuck_t, stuck_sig, not stuck_val)]
            events += [(stuck_t+10, stuck_sig, not stuck_val)]

            times, states = tr.traceSA(init, events, output_signals, stuck_sig, stuck_val, stuck_t, T=T, monitor=True, tokens=tokens, input_widths=input_widths, output_widths=output_widths)

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
        if fault == 'SET':
            ret = check.check(
                    times=times,
                    states=states,
                    events=events,
                    signals=list(init.keys()),
                    output_signals=output_signals,
                    cutoff_min=cutoff_min,
                    cutoff_max=cutoff_max,
                    monitor=True,
                    tokens=tokens,
                    input_widths=input_widths,
                    output_widths=output_widths,
                    victim_signals=[]   # 'd1__chin_op.T', 'b1__c_b_out_0'
            )
            # pprint.pprint(ret)

            plotting.plot(
                    times,
                    states,
                    list(init.keys()),
                    susceptible=ret['susceptible'],
                    cutoff=[cutoff_min, cutoff_max],
                    )
        # else:
        #     ret = check.checkSA(
        #         times=times,
        #         events=events,
        #         states=states,
        #         signals=list(init.keys()),
        #         output_signals=output_signals, 
        #         cutoff_min=cutoff_min,
        #         cutoff_max=cutoff_max,
        #         fault=fault,
        #     )
        #     pprint.pprint(ret)

        #     plotting.plot(
        #         times,
        #         states,
        #         list(init.keys()),
        #         susceptible=ret['susceptible'],
        #         fault=fault,
        #         cutoff=[cutoff_min, cutoff_max],
        #         )

if (__name__ == "__main__"):
    main()

