import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../../')

import pprint
from libs import tracem as tr
from libs import plotting
# from libs import checkbi as check
# from depricated import check
from libs import checkdelta as check
from libs import preprocessing as p

# fault = 'SET'
# fault = 'SA0'
# fault = 'SA1'
fault = 'SAF'

# circuit
# 1 dual-rail-bit 3-stage ring (fast environment)

# inv1
tr.rise(f=tr.INVr, i=['ack2'], o='en1', d=2)
tr.fall(f=tr.INVf, i=['ack2'], o='en1', d=2)

# c1F
tr.rise(f=tr.Cr, i=['c3T','en1'], o='c1F', d=5)
tr.fall(f=tr.Cf, i=['c3T','en1'], o='c1F', d=5)

# c1T
tr.rise(f=tr.Cr, i=['c3F','en1'], o='c1T', d=5)
tr.fall(f=tr.Cf, i=['c3F','en1'], o='c1T', d=5)

# or1
tr.rise(f=tr.ORr, i=['c1F','c1T'], o='ack1', d=4)
tr.fall(f=tr.ORf, i=['c1F','c1T'], o='ack1', d=4)

#######################################################

# inv2
tr.rise(f=tr.INVr, i=['ack3'], o='en2', d=2)
tr.fall(f=tr.INVf, i=['ack3'], o='en2', d=2)

# c2F
tr.rise(f=tr.Cr, i=['c1F','en2'], o='c2F', d=5)
tr.fall(f=tr.Cf, i=['c1F','en2'], o='c2F', d=5)

# c2T
tr.rise(f=tr.Cr, i=['c1T','en2'], o='c2T', d=5)
tr.fall(f=tr.Cf, i=['c1T','en2'], o='c2T', d=5)

# or2
tr.rise(f=tr.ORr, i=['c2F','c2T'], o='ack2', d=4)
tr.fall(f=tr.ORf, i=['c2F','c2T'], o='ack2', d=4)

#######################################################

# inv3
tr.rise(f=tr.INVr, i=['ack1'], o='en3', d=2)
tr.fall(f=tr.INVf, i=['ack1'], o='en3', d=2)

# c3F
tr.rise(f=tr.Cr, i=['c2F','en3'], o='c3F', d=5)
tr.fall(f=tr.Cf, i=['c2F','en3'], o='c3F', d=5)

# c3T
tr.rise(f=tr.Cr, i=['c2T','en3'], o='c3T', d=5)
tr.fall(f=tr.Cf, i=['c2T','en3'], o='c3T', d=5)

# or3
tr.rise(f=tr.ORr, i=['c3F','c3T'], o='ack3', d=4)
tr.fall(f=tr.ORf, i=['c3F','c3T'], o='ack3', d=4)

#######################################################
# pprint.pprint(rules)
# pprint.pprint(signals)

# run it

# init = {'a': 1, 'b': 1, 'y': 0}
# events = [
# 	(0, 'y', 0.5),  # add glitch
# ]
# times, states = tr.trace(init, events=events, T=20)

init = {
	'en1': 1,
	'c1F': 0,
	'c1T': 0,
	'ack1': 0,
	'en2': 0,
	'c2F': 0,
	'c2T': 0,
	'ack2': 0,
	'en3': 1,
	'c3F': 0,
	'c3T': 1,
	'ack3': 1,
}

output_signals=['c3F', 'c3T', 'ack1']

T=100

# cutoff
cutoff_min = 0
cutoff_max = float('Inf')

glitch_t = 4
events = [
    # (glitch_t, 'c3', .5),  # add glitch
    # (glitch_t + 0.1, 'c3', 0),  # reset glitch
]
times, states = tr.trace(init, events, output_signals, T=T)

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])

# ret = check.check(times=times, events=events, states=states, signals=list(init.keys()), output_signals=output_signals)
# pprint.pprint(ret)

# plotting.plot(times, states, list(init.keys()), susceptible=ret['susceptible'])


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
			susceptible=ret['susceptible'],
			cutoff=[cutoff_min, cutoff_max],
			fname="ring_1DRBit_3Stages.svg"
			)
	
else:
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
	# print(f"Susceptible SA1: {susceptible_SA1}")
	# print(f"Susceptible SA0: {susceptible_SA0}")

	susceptible = susceptible_SA1 + susceptible_SA0

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
		fname="ring_1DRBit_3Stages.svg"
		)

