import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../')

import pprint
from libs import tracem as tr
from libs import plotting
# from libs import checkbi as check
# from depricated import check
from libs import preprocessing as p

CHECK = True
# CHECK = False
# fault = 'SET'
# fault = 'SA0'
# fault = 'SA1'
fault = 'SAF'
T=50

#--------|---------|---------|---------|---------|
if fault == 'SET':
	from libs import checkbi as check
else:
	from depricated import check
#--------|---------|---------|---------|---------|

# circuit

# c
tr.rise(f=tr.Cr, i=['a', 'b'], o='y', d=1.5)
tr.fall(f=tr.Cf, i=['a', 'b'], o='y', d=1.5)

init = {
		# 'a': 0,
		# 'b': 1,
		# 'y': 1,
		'a': 0,
		'b': 0,
		'y': 0,
		}

events = [
		# (16, 'b', 0),
		# (28, 'b', 1),

		# (10, 'a', 1),
		# (14, 'a', 0),
		# (18, 'a', 1),
		# (22, 'a', 0),
		# (26, 'a', 1),
		# (30, 'a', 0),
		# (34, 'a', 1),

		(10, 'a', 1),  
		# (11, 'a', 0),
		# (12, 'a', 1),
		(13, 'a', 0),
		(14, 'a', 1),
		# (15, 'a', 0),
		# (16, 'a', 1),
		(17, 'a', 0),
		(18, 'a', 1),
		# (19, 'a', 0),
		# (20, 'a', 1),
		(21, 'a', 0),

]

output_signals = [
		'y',
		# 'a',
]

if not CHECK:
	if fault == 'SET':
		glitch_t = 2
		glitch_sig = 'a'
		events += [
					(glitch_t, glitch_sig, 1),  # add glitch
					(glitch_t + 0.1, glitch_sig, 0),  # reset glitch
			]
#     events += [
#             (2, 'a', 1),  # add glitch
#             (2.1, 'a', 0),  # reset glitch
#             # (5, 'b', 0),  # add glitch
#             # (5.1, 'b', 1),  # reset glitch
#             # (12, 'b', 0),  # add glitch
#             # (14.1, 'b', 1),  # reset glitch
#             # (16, 'a', 0),  # add glitch
#             # (16.1, 'a', 1),  # reset glitch
#             # (26, 'a', 1),  # add glitch
#             # (26.9, 'a', 0),  # reset glitch
#             (27, 'b', 1),  # add glitch
#             (27.1, 'b', 0),  # reset glitch
#     ]

		times, states = tr.trace(init, events, output_signals, T=T)
		
	elif fault == 'SAF' or fault == 'SA1':
		stuck_sig = 'b'
		stuck_value = 1
		stuck_t = 18.5
		
		events += [
			(stuck_t, stuck_sig, stuck_value),
		]
		times, states = tr.traceSA(init, events, output_signals, stuck_sig, stuck_value, stuck_t, T=T)
		# init, events, output_signals, stuck_sig, stuck_value, stuck_t, T=T

		# elif fault == 'SAF' or fault == 'SA0': pass
	 
else:
	times, states = tr.trace(init, events, output_signals, T=T)

plotting.plot(times, states, list(init.keys()), fname="main-c.svg")

# print it
for i in range(len(times)):
		print()
		print(f'time {times[i]}:')
		pprint.pprint(states[i])
		
# cutoff
cutoff_min = 0
cutoff_max = float('Inf')

if CHECK:
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

	susceptible_SA1 = p.appendSAF(p.collapseRanges(SA1_M['susceptible'] if SA1_M else []), 'SA1')
	susceptible_SA0 = p.appendSAF(p.collapseRanges(SA0_M['susceptible']if SA0_M else []), 'SA0')

	susceptible = susceptible_SA1 + susceptible_SA0

	plotting.plot(
			times,
			states,
			list(init.keys()),
			susceptible=susceptible,
			fault=fault,
			cutoff=[cutoff_min, cutoff_max],
			fname="main-c.svg"
			)
