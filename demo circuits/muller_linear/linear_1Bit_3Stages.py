from docopt import docopt
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../../')

import time
import pprint
# from prs import linear_1Bit_3Stages as 
from prs import muller_linear as linear
from libs import tracem as tr
from libs import plotting
from libs import preprocessing as p
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
--fault=F                   Fault type to check (possible values: SET, SA0, SA1, SAF)
                            [default: SAF].
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
        # from libs import checkbi as check
        from libs import checkdelta as check
#--------|---------|---------|---------|---------|

    T = int(options["--runtime"])
    fault = str(options["--fault"])
    assert (fault in ['SET', 'SAF', 'SA1', 'SA0']), "Fault type not supported"

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

            times, states = tr.trace(init, events, output_signals, T=T)

        elif fault == 'SA1':
            # stuck_t = 4
            # stuck_sig = 'c2'
            # stuck_value = 1
            # stuck_t = 30.5
            # stuck_sig = 'en1'
            # stuck_value = 1
            # stuck_t = 23.5
            stuck_sig = 'c_in'
            stuck_value = 1
            stuck_t = 12.999
            events += [
                    # (stuck_t, 'en2', 1),  # add SA1
                    # (24.5, 'en2', 1),  # add SA1
                    # (3.5, 'c2', 1),  # add SA1               #########################
                    (stuck_t, stuck_sig, stuck_value),  # add SA1 
            ]

            # checking that it will stay stuck
            events += [(stuck_t, stuck_sig, not stuck_value)]
            events += [(stuck_t+10, stuck_sig, not stuck_value)]

            times, states = tr.traceSA(init, events, output_signals, stuck_sig, stuck_value, stuck_t, T=T)

        elif fault == 'SA0':
            stuck_value = 0

            stuck_sig = 'c2'
            stuck_t = 19

            stuck_sig = 'en2'
            stuck_t = 9.001

            events += [
                    # (20, 'c1', 0),  
                    # (20, 'en2', 0),
                    # (20.1, 'c1', 0),
                    # (20.1, 'en2', 0),
                    
                    (stuck_t, stuck_sig, 0),  # add SA0
            ]

            # checking that it will stay stuck
            events += [(stuck_t, stuck_sig, not stuck_value)]
            events += [(stuck_t+10, stuck_sig, not stuck_value)]

            times, states = tr.traceSA(init, events, output_signals, stuck_sig, stuck_value, stuck_t, T=T)

        else:
            raise Exception("SAF can only be combined with CHECK")

    # if CHECK, run golden run without any faults
    else:
        times, states = tr.trace(init, events, output_signals, T=T)


    plotting.plot(
        times,
        states,
        list(init.keys()),
        init,
        events,
        delays={},
        fname="linear_1Bit_3Stages.svg"
        )

    # print it
    for i in range(len(times)):
        print()
        print(f'time {times[i]}:')
        pprint.pprint(states[i])

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
                    # victim_signals=['c_in', 'en1']
            )
            pprint.pprint(ret)

            plotting.plot(
                    times,
                    states,
                    list(init.keys()),
                    init,
                    events,
                    delays={},
                    susceptible=ret['susceptible'],
                    fault=fault,
                    cutoff=[cutoff_min, cutoff_max],
                    fname="linear_1Bit_3Stages.svg"
                    )
            
        else:
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
                    # victim_signals=[]
                )
                pprint.pprint(SA1_M)

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
                    # victim_signals=[]
                )
                pprint.pprint(SA0_M)

            end = time.time()

            susceptible_SA1 = p.appendSAF(p.collapseRanges(SA1_M['susceptible'] if SA1_M else []), 'SA1')
            susceptible_SA0 = p.appendSAF(p.collapseRanges(SA0_M['susceptible']if SA0_M else []), 'SA0')
            # print(f"Susceptible SA1: {susceptible_SA1}")
            # print(f"Susceptible SA0: {susceptible_SA0}")

            susceptible = susceptible_SA1 + susceptible_SA0

            total_time = end - start
            print(f"\n time to check circuit using checkdelta is {total_time}")

            plotting.plot(
                times,
                states,
                list(init.keys()),
                init,
                events,
                delays={},
                susceptible=susceptible,
                fault=fault,
                cutoff=[cutoff_min, cutoff_max],
                fname="linear_1Bit_3Stages.svg"
                )
   

if (__name__ == "__main__"):
    main()
