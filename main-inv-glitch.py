import pprint
import tracem as tr
import plotting

# ---- testing ------

# circuit

# inv
tr.rise(f=tr.INVr, i=['i'], o='o', d=1)
tr.fall(f=tr.INVf, i=['i'], o='o', d=1)

init = {'i': 0, 'o': 1,}
glitch_t = 1.5
events = [
	(1, 'i', 1),
	(glitch_t, 'i', 0),  # add down
	# (3, 'i', 1),
]
times, states = tr.trace(init, events=events, T=4)

plotting.plot(times, states, list(init.keys()))

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])
