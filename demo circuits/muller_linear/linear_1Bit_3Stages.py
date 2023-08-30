import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../../')

import pprint
from libs import tracem as tr
from libs import plotting
from libs import checkbi as check

# CHECK = True --> show sensitivity windows
# CHECK = False --> show effect of specific glitches
CHECK = True

# circuit
# Muller Pipeline (linear)
# 1-bit 3-stage linear pipeline

# inv1 (source)
tr.rise(f=tr.INVr, i=['c1'], o='c_in', d=4)
tr.fall(f=tr.INVf, i=['c1'], o='c_in', d=4)

# inv2
tr.rise(f=tr.INVr, i=['c2'], o='en1', d=1)
tr.fall(f=tr.INVf, i=['c2'], o='en1', d=1)

# c1
tr.rise(f=tr.Cr, i=['c_in','en1'], o='c1', d=5)
tr.fall(f=tr.Cf, i=['c_in','en1'], o='c1', d=5)

# inv3
tr.rise(f=tr.INVr, i=['c3'], o='en2', d=1)
tr.fall(f=tr.INVf, i=['c3'], o='en2', d=1)

# c2
tr.rise(f=tr.Cr, i=['c1','en2'], o='c2', d=5)
tr.fall(f=tr.Cf, i=['c1','en2'], o='c2', d=5)

# inv4 (sink)
tr.rise(f=tr.INVr, i=['c3'], o='en3', d=4)
tr.fall(f=tr.INVf, i=['c3'], o='en3', d=4)

# c3
tr.rise(f=tr.Cr, i=['c2','en3'], o='c3', d=5)
tr.fall(f=tr.Cf, i=['c2','en3'], o='c3', d=5)

# pprint.pprint(rules)
# pprint.pprint(signals)

# run it
init = {
	'c_in': 0,
	'en1': 1,
	'c1': 0,
	'en2': 1,
	'c2': 0,
	'en3': 1,
	'c3': 0,
}

events = [
]

if not CHECK:
    glitch_t = 4
    events += [
            (glitch_t, 'c_in', 1),  # add glitch
            (glitch_t + 0.1, 'c_in', 0),  # reset glitch
    ]

times, states = tr.trace(init, events=events, T=32)

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
    ret = check.check(
            times=times,
            events=events,
            states=states,
            signals=list(init.keys()),
            output_signals=['c3', 'c1'],
            cutoff_min=cutoff_min,
            cutoff_max=cutoff_max
    )
    pprint.pprint(ret)

    plotting.plot(
            times,
            states,
            list(init.keys()),
            susceptible=ret['susceptible'],
            cutoff=[cutoff_min, cutoff_max],
            )

