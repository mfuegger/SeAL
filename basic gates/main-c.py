import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../')

import pprint
from libs import tracem as tr
from libs import plotting
from libs import checkbi as check

# CHECK = True --> show sensitivity windows
# CHECK = False --> show effect of specific glitches
CHECK = True

# circuit

# c
tr.rise(f=tr.Cr, i=['a', 'b'], o='y', d=4)
tr.fall(f=tr.Cf, i=['a', 'b'], o='y', d=4)

init = {'a': 0,
	'b': 1,
        'y': 0,}

events = [
	(7, 'a', 1),
	(20, 'b', 0),
	(25, 'a', 0),
]

if not CHECK:
    events += [
            (2, 'a', 1),  # add glitch
            (2.1, 'a', 0),  # reset glitch
            # (5, 'b', 0),  # add glitch
            # (5.1, 'b', 1),  # reset glitch
            # (12, 'b', 0),  # add glitch
            # (14.1, 'b', 1),  # reset glitch
            # (16, 'a', 0),  # add glitch
            # (16.1, 'a', 1),  # reset glitch
            # (26, 'a', 1),  # add glitch
            # (26.9, 'a', 0),  # reset glitch
            (27, 'b', 1),  # add glitch
            (27.1, 'b', 0),  # reset glitch
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
            output_signals=['y'],
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
