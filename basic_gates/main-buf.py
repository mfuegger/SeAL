import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../')

import pprint
from libs import tracem as tr
from libs import plotting

# circuit

# inv
tr.rise(f=tr.BUFr, i=['in'], o='out', d=1)
tr.fall(f=tr.BUFf, i=['in'], o='out', d=1)

init = {'in': 0, 'out': 0,}
glitch_t = 1.5
events = [
	(1, 'in', 1),
	(glitch_t, 'in', 0),  # add down
	(3, 'in', 1),
]
times, states = tr.trace(init, events=events, T=4)

plotting.plot(times, states, list(init.keys()))

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])
