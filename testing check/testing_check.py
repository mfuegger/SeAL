from docopt import docopt
import os
import sys
import subprocess

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../')

from prs import muller_linear as linear
from libs import tracem as tr
from libs import checkbi as check1
from depricated import check as check2


usage_msg = """

TODO
Explain what the script does
cutoff


usage:
    testing_check.py [options]

Options:
-h --help                   Show this screen.
-v --version                Show version information.

--runtime=T                 Time for execution prefix.
                            [default: 100].                   
--cutoff-min=N              The minimal cutoff. the start of the window to investigate
                            [default: 0].
--cutoff-max=N              The maximal cutoff. the end of the window to investigate
                            [default: float('Inf')].               
"""
#--------|---------|---------|---------|---------|---------|---------|---------|


def main():
    options = docopt(usage_msg, version="0.1")

    fault = ['SA0', 'SA1']
    T = int(options["--runtime"])
    
    cutoff_min = int(options["--cutoff-min"])
    cutoff_max = float(options["--cutoff-min"])
    # print(cutoff_max)

    # init = {}
    # events = {}

    script_path = os.path.join(dir_path, "..", 'prs', 'muller_linear')
    for filename in os.listdir(script_path):
        if filename.startswith('linear') and filename.endswith('.py'):
            # if(filename != "linear_scale_DRBits_stages.py"):
            #     continue
            # if(filename != "linear_1Bit_3Stages.py"):
            #     continue
            module_name = os.path.splitext(filename)[0]
            module = getattr(linear, module_name)
            # print(module)

            # create circuit
            tr.clear()
            init, events, output_signals = module.GeneratePipeline()
            # print(init)

            # module = __import__(f'prs.muller_linear.{module_name}', fromlist=[module_name])
            # init, events, output_signals = getattr(module, 'GeneratePipeline')()

            # create circuit
            # init, events = linear.linear_1Bit_3Stages.GeneratePipeline()
            # linear_1Bit_3Stages.GeneratePipeline()

            times, states = tr.trace(init, events=events, T=T)
            # print(states)

            for f in fault:
                ret1 = check1.checkSA(
                    times=times,
                    events=events,
                    states=states,
                    signals=list(init.keys()),
                    output_signals=output_signals,
                    cutoff_min=cutoff_min,
                    cutoff_max=cutoff_max,
                    fault=f,
                )
                # pprint.pprint(ret1)

                ret2 = check2.checkSA(
                    times=times,
                    events=events,
                    states=states,
                    signals=list(init.keys()),
                    output_signals=output_signals,
                    cutoff_min=cutoff_min,
                    cutoff_max=cutoff_max,
                    fault=f,
                )
                # pprint.pprint(ret2)

                # susceptible is a list
                # each item is a tuple of signal and range, e.g., ('c_in', [0, 4])
                susceptible1 =  ret1['susceptible']
                susceptible2 =  ret2['susceptible']

                # intervals_per_sig a dictionary
                # each value item is a list of ranges, e.g., ('c_in', [0, 4], [6, 10], [15, 17])
                intervals1_per_sig = {}
                intervals2_per_sig = {}

                for s in susceptible1:
                    sig = s[0]
                    range = s[1]
                    # print(f'current signal = {sig} and current range = {range}')
                    if sig in intervals1_per_sig:
                        last_added_range = intervals1_per_sig[sig][-1]
                        # print(f'last added range = {last_added_range} and last_to in range = {last_added_range[1]}')
                        if  last_added_range[1] == range[0]: 
                            intervals1_per_sig[sig][-1] = [last_added_range[0], range[1]] 
                            # print(f'new range = {intervals1_per_sig[sig][-1]}')              
                        else:
                            intervals1_per_sig[sig].append(range)
                    else:
                        intervals1_per_sig[sig] = [range]

                for s in susceptible2:
                    sig = s[0]
                    range = s[1]
                    # print(f'current signal = {sig} and current range = {range}')
                    if sig in intervals2_per_sig:
                        last_added_range = intervals2_per_sig[sig][-1]
                        # print(f'last added range = {last_added_range} and last_to in range = {last_added_range[1]}')
                        if  last_added_range[1] == range[0]: 
                            intervals2_per_sig[sig][-1] = [last_added_range[0], range[1]] 
                            # print(f'new range = {intervals2_per_sig[sig][-1]}')              
                        else:
                            intervals2_per_sig[sig].append(range)
                    else:
                        intervals2_per_sig[sig] = [range]   

                print(f'--------------------------------------{f}-----------------------------------------------')
                for sig in intervals1_per_sig.keys():
                    print('-------------------------------------------------------------------------')
                    print(sig, intervals1_per_sig[sig])
                    print(sig, intervals2_per_sig[sig])

                print('-------------------------------------------------------------------------')
                for sig in intervals1_per_sig.keys():
                    set1 = {(sig, tuple(item)) for item in intervals1_per_sig[sig]}

                for sig in intervals2_per_sig.keys():
                    set2 = {(sig,tuple(item)) for item in intervals2_per_sig[sig]}

                unique_to_list1 = set1 - set2
                unique_to_list2 = set2 - set1

                unique_to_checkbi = [{'key': key, 'values': list(values)} for key, values in unique_to_list1]
                unique_to_check = [{'key': key, 'values': list(values)} for key, values in unique_to_list2]

                if(not unique_to_checkbi and not unique_to_check):
                # if ret1['susceptible'] == ret2['susceptible']:
                    print("Alles gut!")
                else:
                    print("ERROR")
                    print("Unique to checkbi:", unique_to_checkbi)
                    print("Unique to check:", unique_to_check)
                print('-------------------------------------------------------------------------------------')


if (__name__ == "__main__"):
    main()