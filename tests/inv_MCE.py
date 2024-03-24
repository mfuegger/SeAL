import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../')

import pprint
from libs import tracem as tr
from libs import plotting
# from depricated import check
from libs import checkbi as check

# CHECK = False
CHECK = True
fault = 'SET'
# fault = 'SA0'
# fault = 'SA1'

# circuit

# inv1
# tr.rise(f=tr.INVr, i=['a5'], o='a1', d=1)
# tr.fall(f=tr.INVf, i=['a5'], o='a1', d=1)

# inv2
tr.rise(f=tr.INVr, i=['c1'], o='a2', d=1.3)
tr.fall(f=tr.INVf, i=['c1'], o='a2', d=1.3)

# inv3
tr.rise(f=tr.INVr, i=['a2'], o='a3', d=1.1)
tr.fall(f=tr.INVf, i=['a2'], o='a3', d=1.1)

# inv4
tr.rise(f=tr.INVr, i=['a3'], o='a4', d=0.9)
tr.fall(f=tr.INVf, i=['a3'], o='a4', d=0.9)

# MCE1
tr.rise(f=tr.Cr, i=['a4','a5'], o='c1', d=1.6)
tr.fall(f=tr.Cf, i=['a4','a5'], o='c1', d=1.6)

# inv5
tr.rise(f=tr.INVr, i=['c1'], o='a5', d=0.96)
tr.fall(f=tr.INVf, i=['c1'], o='a5', d=0.96)

init = {
	# 'a1': 1,
	'a2': 0,
	'a3': 1,
	'a4': 0,
	'c1': 0,
	'a5': 1,
}

events = [
]

T = 70

if not CHECK:
	if fault == 'SET':
		glitch_t = 25.4
		glitch_sig = 'a2'
		events += [
				(glitch_t, glitch_sig, 0.5),  # add glitch
				(glitch_t + 0.1, glitch_sig, 1),  # reset glitch
		]
		times, states = tr.trace(init, events=events, output_signals=['c1'], T=T)
		# times, states = tr.traceSA(init, events=events, SA_sig='a1', SA_time=glitch_t, T=T)
	
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

		times, states = tr.traceSA(init, events, ['c1'], stuck_sig, stuck_val, stuck_t, T=T)

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

		times, states = tr.traceSA(init, events, ['c1'], stuck_sig, stuck_val, stuck_t, T=T)
		# , monitor=True, tokens=tokens, input_widths=input_widths, output_widths=output_widths
else:
	times, states = tr.trace(init, events=events, output_signals=['c1'], T=T)

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
	if fault == 'SET':
		ret = check.check(
				times=times,
				states=states,
				events=events,
				signals=list(init.keys()),
				output_signals=['c1'],
				cutoff_min=cutoff_min,
				cutoff_max=cutoff_max,
				# monitor=True,
				# tokens=tokens,
				# input_widths=input_widths,
				# output_widths=output_widths,
				# sig='d1__chin_op.T'
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
