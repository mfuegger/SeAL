import pprint
import trace as tr
import plotting

# ---- testing ------

# circuit

# c
tr.rise(f=tr.Cr, i=['a','b'], o='y', d=2)
tr.fall(f=tr.Cf, i=['a','b'], o='y', d=2)

# inv
tr.rise(f=tr.INVr, i=['y'], o='a', d=4)
tr.fall(f=tr.INVf, i=['y'], o='a', d=4)

# inv
tr.rise(f=tr.INVr, i=['y'], o='b', d=5)
tr.fall(f=tr.INVf, i=['y'], o='b', d=5)

# inv
#rise(f=INVr, i=['y'], o='z', d=1)
#fall(f=INVf, i=['y'], o='z', d=1)

# pprint.pprint(rules)
# pprint.pprint(signals)

# run it
init = {'a': 1, 'b': 1, 'y': 0}
events = [
	(0, 'y', 0.5),  # add glitch
]
times, states = tr.trace(init, events=events, T=20)
plotting.plot(times, states)

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])
