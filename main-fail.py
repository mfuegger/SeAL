import pprint
import trace as tr
import plotting

# ---- testing ------

# circuit

# c
# tr.rise(f=tr.Cr, i=['a','b'], o='y', d=2)
# tr.fall(f=tr.Cf, i=['a','b'], o='y', d=2)

# # inv
# tr.rise(f=tr.INVr, i=['y'], o='a', d=4)
# tr.fall(f=tr.INVf, i=['y'], o='a', d=4)

# # inv
# tr.rise(f=tr.INVr, i=['y'], o='b', d=5)
# tr.fall(f=tr.INVf, i=['y'], o='b', d=5)

# inv5
tr.rise(f=tr.INVr, i=['c1'], o='c_in', d=4)
tr.fall(f=tr.INVf, i=['c1'], o='c_in', d=4)

# inv1
tr.rise(f=tr.INVr, i=['c2'], o='en1', d=2)
tr.fall(f=tr.INVf, i=['c2'], o='en1', d=2)

# c1
tr.rise(f=tr.Cr, i=['c_in','en1'], o='c1', d=5)
tr.fall(f=tr.Cf, i=['c_in','en1'], o='c1', d=5)

# inv2
tr.rise(f=tr.INVr, i=['c3'], o='en2', d=2)
tr.fall(f=tr.INVf, i=['c3'], o='en2', d=2)

# c2
tr.rise(f=tr.Cr, i=['c1','en2'], o='c2', d=5)
tr.fall(f=tr.Cf, i=['c1','en2'], o='c2', d=5)

# inv3
tr.rise(f=tr.INVr, i=['c3'], o='en3', d=4)
tr.fall(f=tr.INVf, i=['c3'], o='en3', d=4)

# c3
tr.rise(f=tr.Cr, i=['c2','en3'], o='c3', d=5)
tr.fall(f=tr.Cf, i=['c2','en3'], o='c3', d=5)

# # inv4
# tr.rise(f=tr.INVr, i=['c3'], o='ack_in', d=4)
# tr.fall(f=tr.INVf, i=['c3'], o='ack_in', d=4)

# inv
#rise(f=INVr, i=['y'], o='z', d=1)
#fall(f=INVf, i=['y'], o='z', d=1)

# pprint.pprint(rules)
# pprint.pprint(signals)

# run it

# init = {'a': 1, 'b': 1, 'y': 0}
# events = [
# 	(0, 'y', 0.5),  # add glitch
# ]
# times, states = tr.trace(init, events=events, T=20)

init = {'c_in': 0, 'en1': 1, 'c1': 0, 'en2': 1, 'c2': 0, 'en3': 1, 'c3': 0,}
glitch_t = 10
events = [
    (glitch_t, 'en1', 1),  # add glitch
    (glitch_t + 0.1, 'en1', 0),  # reset glitch
]
times, states = tr.trace(init, events=events, T=32)

plotting.plot(times, states, list(init.keys()))

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])
