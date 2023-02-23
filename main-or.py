import pprint
import tracem as tr
import plotting

# ---- testing ------

# circuit

# or
tr.rise(f=tr.ORr, i=['a', 'b'], o='y', d=4)
tr.fall(f=tr.ORf, i=['a', 'b'], o='y', d=4)

init = {'a': 0, 'b': 1, 'y': 0,}
events = [
	(5, 'a', 1),  # add glitch
	(5.1, 'a', 0),  # reset glitch
    (10, 'a', 0),  # add glitch
	(10.1, 'a', 1),  # reset glitch
	(10, 'b', 0),  # add glitch
	(10.1, 'b', 1),  # reset glitch
	(7, 'a', 1),
	# (12, 'b', 0),  # add glitch
	# (14.1, 'b', 1),  # reset glitch
	(22, 'a', 0),  # add glitch
	(22.1, 'a', 1),  # reset glitch
	(20, 'b', 0),
	# (26, 'a', 1),  # add glitch
	# (26.9, 'a', 0),  # reset glitch
	(27, 'a', 0),
    (8.5, 'b', 0),  # add glitch
	(8.6, 'b', 1),  # reset glitch
	(31.5, 'a', 1),  # add glitch
	(31.6, 'a', 0),  # reset glitch
]
times, states = tr.trace(init, events=events, T=40)

plotting.plot(times, states, list(init.keys()))

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])
