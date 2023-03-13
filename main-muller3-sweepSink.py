import pprint
import tracem as tr
import plotting
import checknew as check
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def createCircuit(sink_delay):
	# circuit
	# Muller Pipeline (linear)

	# inv1 (source)
	tr.rise(f=tr.INVr, i=['c1'], o='c_in', d=4)
	tr.fall(f=tr.INVf, i=['c1'], o='c_in', d=4)

	# inv2
	tr.rise(f=tr.INVr, i=['c2'], o='en1', d=1)
	tr.fall(f=tr.INVf, i=['c2'], o='en1', d=1)

	# c1
	tr.rise(f=tr.Cr, i=['c_in','en1'], o='c1', d=5)
	tr.fall(f=tr.Cf, i=['c_in','en1'], o='c1', d=5)

	# inv3
	tr.rise(f=tr.INVr, i=['c3'], o='en2', d=1)
	tr.fall(f=tr.INVf, i=['c3'], o='en2', d=1)

	# c2
	tr.rise(f=tr.Cr, i=['c1','en2'], o='c2', d=5)
	tr.fall(f=tr.Cf, i=['c1','en2'], o='c2', d=5)

	# inv4
	tr.rise(f=tr.INVr, i=['c3'], o='en3', d=sink_delay)
	tr.fall(f=tr.INVf, i=['c3'], o='en3', d=sink_delay)

	# c3
	tr.rise(f=tr.Cr, i=['c2','en3'], o='c3', d=5)
	tr.fall(f=tr.Cf, i=['c2','en3'], o='c3', d=5)


T = 200
sweep_values = np.linspace(1, 25, num=25)
results = {}

plt.figure()
labels = []
markers = []
i = 0

for source_delay in range(4, 25, 6):

    labels.append(f'sink delay = {source_delay}')

    results[source_delay] = {'snk_delay':[], 'p':[]}

    for sink_delay in tqdm(sweep_values):
            # clear circuit
            tr.clear()
            
            # create it
            createCircuit(sink_delay=sink_delay)

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
            results[source_delay]['snk_delay'] += [sink_delay]
            results[source_delay]['p'] += [ret['p']]

    plt.plot(results[source_delay]['snk_delay'], results[source_delay]['p'], linestyle='-', marker='o', label=labels[i])
    i += 1


plt.xlabel('sink delay [INV delay]')
plt.ylabel('P(fail)')
# plt.plot(sweep_values, p, '*', color='blue')
plt.xlim(0, 25+0.5)
plt.ylim(0,1)
plt.legend(loc=3)

fname = 'muller3_sweepSink.png'
print(f'[info] saving figure: {fname}')
plt.savefig(
    fname,
    dpi=300,
    format='png',
    metadata=None,
    bbox_inches=None,
    pad_inches=0.01,
    facecolor='auto',
    edgecolor='auto'
)

# plot the last one
plotting.plot(
	times,
	states,
	list(init.keys()),
	susceptible=ret['susceptible'],
	cutoff=[cutoff_min, cutoff_max],
	)

# plt.show()