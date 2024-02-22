from docopt import docopt
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../../')

import pprint
# from prs import linear_1Bit_3Stages as 
from prs import muller_linear as linear
from libs import tracem as tr
from libs import plotting
# from libs import checkbi as check
# from depricated import check

    # linear1_Bit_3Stages.py [-c | --check]
    # linear1_Bit_3Stages.py -h | -v

usage_msg = """

TODO
Explain what the script does
cutoff


usage:
    linear_1Bit_3Stages.py [options]

Options:
-h --help                   Show this screen.
-v --version                Show version information.

--runtime=T                 Time for execution prefix.
                            [default: 100].                   
-c --check                  Check all sensitivty windows.
--exhaustive                Check by injecting faults exhaustively (depricated version of check for SET).
--fault=F                   Fault type to check (possible values: SET, SA0, SA1)
                            [default: SA1].
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
    if (options["--check"]):
        CHECK = True
    else:
        CHECK = False

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
    init, events, output_signals = linear.linear_1Bit_3Stages.GeneratePipeline()

    if not CHECK:
        if fault == 'SET':
            glitch_t = 7.9
            glitch_sig = 'c2'
            events += [
                    (glitch_t, glitch_sig, 1),  # add glitch
                    (glitch_t + 0.1, glitch_sig, 0),  # reset glitch
            ]

            times, states = tr.trace(init, events=events, T=T)

        elif fault == 'SA1':
            stuck_t = 4
            stuck_sig = 'c2'
            events += [
                    # (stuck_t, 'en2', 1),  # add SA1
                    # (24.5, 'en2', 1),  # add SA1
                    # (3.5, 'c2', 1),  # add SA1               #########################
                    (stuck_t, stuck_sig, 1),  # add SA1 
            ]

            times, states = tr.traceSA(init, events, stuck_sig, stuck_t, T=T)

        else:
            stuck_t = 15
            stuck_sig = 'c2'
            events += [
                    # (20, 'c1', 0),  
                    # (20, 'en2', 0),
                    # (20.1, 'c1', 0),
                    # (20.1, 'en2', 0),
                    
                    (stuck_t, stuck_sig, 0),  # add SA0
            ]

            times, states = tr.traceSA(init, events=events, SA_sig=stuck_sig, SA_time=stuck_t, T=T)

    # if CHECK, run golden run without any faults
    else:
        times, states = tr.trace(init, events=events, T=T)


    plotting.plot(times, states, list(init.keys()))

    # print it
    for i in range(len(times)):
        print()
        print(f'time {times[i]}:')
        pprint.pprint(states[i])

    if CHECK:
        if fault == 'SET':
            ret = check.check(
                    times=times,
                    events=events,
                    states=states,
                    signals=list(init.keys()),
                    output_signals=output_signals,
                    cutoff_min=cutoff_min,
                    cutoff_max=cutoff_max,
            )
            pprint.pprint(ret)

            plotting.plot(
                    times,
                    states,
                    list(init.keys()),
                    susceptible=ret['susceptible'],
                    cutoff=[cutoff_min, cutoff_max],
                    )
        else:
            ret = check.checkSA(
                times=times,
                events=events,
                states=states,
                signals=list(init.keys()),
                output_signals=output_signals, 
                cutoff_min=cutoff_min,
                cutoff_max=cutoff_max,
                fault=fault,
            )
            pprint.pprint(ret)

            plotting.plot(
                times,
                states,
                list(init.keys()),
                susceptible=ret['susceptible'],
                fault=fault,
                cutoff=[cutoff_min, cutoff_max],
                )

if (__name__ == "__main__"):
    main()
