import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../')

import pprint
from libs import tracem as tr
from libs import plotting
from libs import checkbi as check
# from depricated import check

# CHECK = False
CHECK = True
# fault_check = 'SET'
# fault_check = 'SA0'
fault_check = 'SA1'

# circuit

# MCE1
tr.rise(f=tr.Cr, i=['a1','a1'], o='a2', d=5)
tr.fall(f=tr.Cf, i=['a1','a1'], o='a2', d=5)

# MCE2
tr.rise(f=tr.Cr, i=['a1','a2'], o='a3', d=5)
tr.fall(f=tr.Cf, i=['a1','a2'], o='a3', d=5)

# inv1
tr.rise(f=tr.INVr, i=['a3'], o='a1', d=1)
tr.fall(f=tr.INVf, i=['a3'], o='a1', d=1)


init = {
	'a1': 0,
	'a2': 0,
    'a3': 1,
}

events = [
]

T = 50

if not CHECK:
	# glitch_t = 34
	glitch_t = 22

	events = [
		# (glitch_t, 'a1', 0),
        (glitch_t, 'a1', 1),
	]
	# times, states = tr.traceSA(init, events=events, SA_sig='a1', SA_time=glitch_t, T=T)
	times, states = tr.traceSA(init, events=events, SA_sig='a1', SA_time=glitch_t, T=T)
	
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
            # exclude_output_signals=True,
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
