import pprint
import tracem as tr
import plotting
import check

# ---- testing ------

# circuit
# 1 dual-rail bit ring (fast environment)

# inv1
tr.rise(f=tr.INVr, i=['ack2'], o='en1', d=2)
tr.fall(f=tr.INVf, i=['ack2'], o='en1', d=2)

# c1F
tr.rise(f=tr.Cr, i=['c3T','en1'], o='c1F', d=5)
tr.fall(f=tr.Cf, i=['c3T','en1'], o='c1F', d=5)

# c1T
tr.rise(f=tr.Cr, i=['c3F','en1'], o='c1T', d=5)
tr.fall(f=tr.Cf, i=['c3F','en1'], o='c1T', d=5)

# or1
tr.rise(f=tr.ORr, i=['c1F','c1T'], o='ack1', d=4)
tr.fall(f=tr.ORf, i=['c1F','c1T'], o='ack1', d=4)

#######################################################

# inv2
tr.rise(f=tr.INVr, i=['ack3'], o='en2', d=2)
tr.fall(f=tr.INVf, i=['ack3'], o='en2', d=2)

# c2F
tr.rise(f=tr.Cr, i=['c1F','en2'], o='c2F', d=5)
tr.fall(f=tr.Cf, i=['c1F','en2'], o='c2F', d=5)

# c2T
tr.rise(f=tr.Cr, i=['c1T','en2'], o='c2T', d=5)
tr.fall(f=tr.Cf, i=['c1T','en2'], o='c2T', d=5)

# or2
tr.rise(f=tr.ORr, i=['c2F','c2T'], o='ack2', d=4)
tr.fall(f=tr.ORf, i=['c2F','c2T'], o='ack2', d=4)

#######################################################

# inv3
tr.rise(f=tr.INVr, i=['ack1'], o='en3', d=2)
tr.fall(f=tr.INVf, i=['ack1'], o='en3', d=2)

# c3F
tr.rise(f=tr.Cr, i=['c2F','en3'], o='c3F', d=5)
tr.fall(f=tr.Cf, i=['c2F','en3'], o='c3F', d=5)

# c3T
tr.rise(f=tr.Cr, i=['c2T','en3'], o='c3T', d=5)
tr.fall(f=tr.Cf, i=['c2T','en3'], o='c3T', d=5)

# or3
tr.rise(f=tr.ORr, i=['c3F','c3T'], o='ack3', d=4)
tr.fall(f=tr.ORf, i=['c3F','c3T'], o='ack3', d=4)

#######################################################
# pprint.pprint(rules)
# pprint.pprint(signals)

# run it

# init = {'a': 1, 'b': 1, 'y': 0}
# events = [
# 	(0, 'y', 0.5),  # add glitch
# ]
# times, states = tr.trace(init, events=events, T=20)

init = {
	'en1': 1,
	'c1F': 0,
	'c1T': 0,
	'ack1': 0,
	'en2': 0,
	'c2F': 0,
	'c2T': 0,
	'ack2': 0,
	'en3': 1,
	'c3F': 0,
	'c3T': 1,
	'ack3': 1,
}
glitch_t = 4
events = [
    # (glitch_t, 'c3', .5),  # add glitch
    # (glitch_t + 0.1, 'c3', 0),  # reset glitch
]
times, states = tr.trace(init, events=events, T=32)

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])

ret = check.check(times=times, events=events, states=states, signals=list(init.keys()), output_signals=['c3F', 'c3T', 'ack1'])
pprint.pprint(ret)

plotting.plot(times, states, list(init.keys()), susceptible=ret['susceptible'])

