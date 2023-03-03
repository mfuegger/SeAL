import pprint
import tracem as tr
import plotting
import check
import numpy as np
import matplotlib.pyplot as plt

def createCircuit(source_delay):
	# circuit
	# Muller Pipeline

	# inv5
	tr.rise(f=tr.INVr, i=['c1'], o='c_in', d=source_delay)
	tr.fall(f=tr.INVf, i=['c1'], o='c_in', d=source_delay)

	# inv1
	tr.rise(f=tr.INVr, i=['c2'], o='en1', d=1)
	tr.fall(f=tr.INVf, i=['c2'], o='en1', d=1)

	# c1
	tr.rise(f=tr.Cr, i=['c_in','en1'], o='c1', d=5)
	tr.fall(f=tr.Cf, i=['c_in','en1'], o='c1', d=5)

	# inv2
	tr.rise(f=tr.INVr, i=['c3'], o='en2', d=1)
	tr.fall(f=tr.INVf, i=['c3'], o='en2', d=1)

	# c2
	tr.rise(f=tr.Cr, i=['c1','en2'], o='c2', d=5)
	tr.fall(f=tr.Cf, i=['c1','en2'], o='c2', d=5)

	# inv3
	tr.rise(f=tr.INVr, i=['c3'], o='en3', d=1)
	tr.fall(f=tr.INVf, i=['c3'], o='en3', d=1)

	# c3
	tr.rise(f=tr.Cr, i=['c2','en3'], o='c3', d=5)
	tr.fall(f=tr.Cf, i=['c2','en3'], o='c3', d=5)


T = 50
sweep_values = np.linspace(0.1, 50, num=20)
p = []
for source_delay in sweep_values:
	# clear circuit
	tr.clear()
	
	# create it
	createCircuit(source_delay=source_delay)

	# check it to get p
	init = {
		'c_in': 0,
		'en1': 1,
		'c1': 0,
		'en2': 1,
		'c2': 0,
		'en3': 1,
		'c3': 0,
	}
	events = []
	times, states = tr.trace(init, events=events, T=T)

	# cutoff
	cutoff_min = 0
	cutoff_max = float('Inf')

	ret = check.check(
		times=times,
		events=events,
		states=states,
		signals=list(init.keys()),
		output_signals=['c3', 'c1'],
		cutoff_min=cutoff_min,
		cutoff_max=cutoff_max
	)
	#pprint.pprint(ret)
	p += [ ret['p'] ]


plt.figure()
plt.xlabel('source delay [INV delay]')
plt.ylabel('P(fail)')
plt.plot(sweep_values, p, '*', color='blue')
plt.ylim(0,1)
plt.show()


# plotting.plot(
# 	times,
# 	states,
# 	list(init.keys()),
# 	susceptible=ret['susceptible'],
# 	cutoff=[cutoff_min, cutoff_max],
# 	)
