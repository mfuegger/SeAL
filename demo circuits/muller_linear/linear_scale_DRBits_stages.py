from docopt import docopt
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../../')

import pprint
from prs import linear_scale_DRBits_stages as linear
from libs import tracem as tr
from libs import plotting
# from libs import checkbi as check
# from depricated import check


# CREATE LINEAR PIPELINE w/ VARIABLE NUMBER OF STAGES AND INPUT BITS
# TODO work out automatic initialization
# TODO fix percentages in paper based on monitored signals section A.3


usage_msg = """

TODO
Explain what the script does
cutoff


usage:
    linear_scale_DRBits_stages.py [options]

Options:
-h --help                   Show this screen.
-v --version                Show version information.

--runtime=T                 Time for execution prefix.
                            [default: 100].                   
--exhaustive                Check by injecting faults exhaustively (depricated version of check for SET).
--fault=F                   Fault type to check (possible values: SET, SA0, SA1)
                            [default: SET].
--cutoff-min=N              The minimal cutoff. the start of the window to investigate
                            [default: 0].
--cutoff-max=N              The maximal cutoff. the end of the window to investigate
                            [default: float('Inf')].
--num_stages=N              Number of stages for pipeline
                            [default: 3].
--num_bits=N                Number of input bits (if 2 then actually 4, if 4 then actually 8)
                            [default: 4].       
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

    num_stages = int(options["--num_stages"])
    num_bits = int(options["--num_bits"])

    # create circuit
    init, events, output_signals = linear.GeneratePipeline()  #(num_stages, num_bits)

    times, states = tr.trace(init, events=events, T=T)

    # print it
    # for i in range(len(times)):
    # 	print()
    # 	print(f'time {times[i]}:')
    # 	pprint.pprint(states[i])

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
        
        pprint.pprint(ret['p_per_sig'])
        print(ret['p'])
        plotting.plotSensitivityBars(p_per_sig=ret['p_per_sig'], fname=f'bar-linear-{num_bits}bit.pdf')

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
                fault=fault,
                cutoff_min=cutoff_min,
                cutoff_max=cutoff_max,
        )
        
        pprint.pprint(ret['p_per_sig'])
        print(ret['p'])
        plotting.plotSensitivityBars(p_per_sig=ret['p_per_sig'], fname=f'bar-linear-{num_bits}bit.pdf')

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