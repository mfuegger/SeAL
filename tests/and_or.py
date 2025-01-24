import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../')

import pprint
from seal import tracem as tr
from seal import plotting
# from depricated import check
from seal import checkbi as check

CHECK = False
# CHECK = True
# fault = 'SET'
# fault = 'SA0'
fault = 'SA1'

# circuit

# AND1
tr.rise(f=tr.ANDr, i=['a4','a1'], o='a2', d=5)
tr.fall(f=tr.ANDf, i=['a4','a1'], o='a2', d=5)

# OR1
tr.rise(f=tr.ORr, i=['a2','a1'], o='a3', d=5)
tr.fall(f=tr.ORf, i=['a2','a1'], o='a3', d=5)

# inv1
tr.rise(f=tr.INVr, i=['a3'], o='a4', d=1)
tr.fall(f=tr.INVf, i=['a3'], o='a4', d=1)


init = {
	'a1': 0,
	'a2': 0,
	'a3': 1,
	'a4': 0,
}

events = [
	  (7, 'a1', 1),
	  (19, 'a1', 0),
	  (27, 'a1', 1),
	  (39, 'a1', 0),
]

T = 30

if not CHECK:
	# # glitch_t = 34
	# glitch_t = 22

	# events = [
	# 	# (glitch_t, 'a1', 0),
	# 	(glitch_t, 'a1', 1),
	# ]
	# # times, states = tr.traceSA(init, events=events, SA_sig='a1', SA_time=glitch_t, T=T)
	# times, states = tr.traceSA(init, events=events, SA_sig='a1', SA_time=glitch_t, T=T)
	   
	if fault == 'SA1':
		stuck_sig = 'a2'
		stuck_value = 1
		stuck_t = 19.5
		# stuck_sig = 'a1'
		# stuck_value = 1
		# stuck_t = 38
		events += [
				(stuck_t, stuck_sig, stuck_value),  # add SA1 
		]

		# checking that it will stay stuck
		# events += [(stuck_t+10, stuck_sig, not stuck_value)]

		times, states = tr.traceSA(init, events, stuck_sig, stuck_value, stuck_t, T=T)

	else:
		stuck_sig = 'a2'
		stuck_value = 0
		stuck_t = 19.5
		events += [				
				(stuck_t, stuck_sig, stuck_value),  # add SA0
		]

		# checking that it will stay stuck
		events += [(stuck_t+10, stuck_sig, not stuck_value)]

		times, states = tr.traceSA(init, events, stuck_sig, stuck_value, stuck_t, T=T)
	
else:
	times, states = tr.trace(init, events=events, T=T)

plotting.plot(times, states, list(init.keys()))

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])
	
# cutoff
cutoff_min = 0
cutoff_max = float('Inf')

if CHECK:
	ret = check.checkSA(
			times=times,
			events=events,
			states=states,
			signals=list(init.keys()),
			output_signals=['a3'],
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
