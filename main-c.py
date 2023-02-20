import pprint
import trace as tr
import plotting

# ---- testing ------

# circuit

# inv
tr.rise(f=tr.Cr, i=['a', 'b'], o='y', d=4)
tr.fall(f=tr.Cf, i=['a', 'b'], o='y', d=4)

init = {'a': 0, 'b': 1, 'y': 0,}
events = [
	(2, 'a', 1),  # add glitch
	(2.1, 'a', 0),  # reset glitch
	# (5, 'b', 0),  # add glitch
	# (5.1, 'b', 1),  # reset glitch
	(7, 'a', 1),
	# (12, 'b', 0),  # add glitch
	# (14.1, 'b', 1),  # reset glitch
	# (16, 'a', 0),  # add glitch
	# (16.1, 'a', 1),  # reset glitch
	(20, 'b', 0),
	# (26, 'a', 1),  # add glitch
	# (26.9, 'a', 0),  # reset glitch
	(27, 'b', 1),  # add glitch
	(27.1, 'b', 0),  # reset glitch
	(25, 'a', 0),
]
times, states = tr.trace(init, events=events, T=32)

plotting.plot(times, states, list(init.keys()))

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])
