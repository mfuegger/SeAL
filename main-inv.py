import pprint
import tracem as tr
import plotting

# ---- testing ------

# circuit

# inv
tr.rise(f=tr.INVr, i=['a'], o='y', d=4)
tr.fall(f=tr.INVf, i=['a'], o='y', d=4)

init = {'a': 0, 'y': 0,}
glitch_t = 5
events = [
	# (glitch_t, 'a', 1),  # add glitch
	# (glitch_t + 0.1, 'a', 0),  # reset glitch
	(10, 'a', 1),
	# (glitch_t + 10, 'a', 0),  # add glitch
	# (glitch_t + 10 + 0.1, 'a', 1),  # reset glitch
	(20, 'a', 0),
	# (glitch_t + 20, 'a', 1),  # add glitch
	# (glitch_t + 20 + 0.1, 'a', 0),  # reset glitch
	(30, 'a', 1),
]
times, states = tr.trace(init, events=events, T=32)

plotting.plot(times, states, list(init.keys()))

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])
