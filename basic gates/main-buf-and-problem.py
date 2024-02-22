import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../')

import pprint
from libs import tracem as tr
from libs import plotting
# from libs import checkbi as check
from depricated import check

# CHECK = True --> show sensitivity windows
# CHECK = False --> show effect of specific glitches
# CHECK = False
CHECK = True
# fault_check = 'SET'
fault_check = 'SA0'
# fault_check = 'SA1'

# circuit
# BUFF + AND

# buf
tr.rise(f=tr.BUFr, i=['a'], o='b', d=5)
tr.fall(f=tr.BUFf, i=['a'], o='b', d=5)

# and
tr.rise(f=tr.ANDr, i=['i', 'b'], o='o', d=1)
tr.fall(f=tr.ANDf, i=['i', 'b'], o='o', d=1)

# pprint.pprint(rules)
# pprint.pprint(signals)

# run it
init = {
	'a': 0,
	'b': 0,
	'o': 0,
	'i': 0,
}

events = [
	(10, 'i', 1),  # input transition
	(11, 'a', 1),  # input transition
	(20, 'i', 0),  # input transition
]

if not CHECK:
	glitch_t = 5.1
	events += [
	    (glitch_t,       'a', 0.5),  # add glitch
	    (glitch_t + 0.01, 'a', 0),  # reset glitch
	]

times, states = tr.trace(init, events=events, T=50)

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])

# cutoff
cutoff_min = 0
cutoff_max = float('Inf')

plotting.plot(
	times,
	states,
	list(init.keys()),
	cutoff=[cutoff_min, cutoff_max],
	)

if CHECK:
	ret = check.checkSA(
		times=times,
		events=events,
		states=states,
		signals=list(init.keys()),
		output_signals=['o'],
		cutoff_min=cutoff_min,
		cutoff_max=cutoff_max,
		fault=fault_check,
	)
	pprint.pprint(ret)

	plotting.plot(
		times,
		states,
		list(init.keys()),
		susceptible=ret['susceptible'],
		fault=fault_check,
		cutoff=[cutoff_min, cutoff_max],
		)


