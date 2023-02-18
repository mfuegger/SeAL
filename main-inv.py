import pprint
import trace as tr
import plotting

# ---- testing ------

# circuit

# inv
tr.rise(f=tr.INVr, i=['a'], o='y', d=4)
tr.fall(f=tr.INVf, i=['a'], o='y', d=4)

init = {'a': 0, 'y': 0,}
events = [
	(2, 'a', 1),  # add glitch
	(2.1, 'a', 0),  # reset glitch
]
times, states = tr.trace(init, events=events, T=32)

plotting.plot(times, states, list(init.keys()))

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])
