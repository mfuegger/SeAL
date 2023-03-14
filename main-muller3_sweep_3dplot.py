import pprint
import tracem as tr
import plotting
import checkbi as check
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

import pickle
import pandas as pd
from mpl_toolkits import mplot3d
import argparse
from tqdm import tqdm
from tqdm.contrib import itertools

def createCircuit(source_delay, sink_delay):
    # circuit
    # Muller Pipeline (linear)

    # inv1 (source)
    tr.rise(f=tr.INVr, i=['c1'], o='c_in', d=source_delay)
    tr.fall(f=tr.INVf, i=['c1'], o='c_in', d=source_delay)

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

    # inv4 (sink)
    tr.rise(f=tr.INVr, i=['c3'], o='en3', d=sink_delay)
    tr.fall(f=tr.INVf, i=['c3'], o='en3', d=sink_delay)

    # c3
    tr.rise(f=tr.Cr, i=['c2','en3'], o='c3', d=5)
    tr.fall(f=tr.Cf, i=['c2','en3'], o='c3', d=5)



parser = argparse.ArgumentParser()
parser.add_argument('--generate', action='store_true')
args = parser.parse_args()

T = 1000
NUM = 2 # 25
sweep_values_src = np.linspace(1, 25, num=NUM)
sweep_values_snk = np.linspace(1, 25, num=NUM)

if args.generate:

    print('[info] generating data')

    p = []
    snk = []
    src = []

    for sink_delay, source_delay in itertools.product(sweep_values_snk, sweep_values_src):
        # clear circuit
        tr.clear()
        
        # create it
        createCircuit(source_delay=source_delay, sink_delay=sink_delay)

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
            cutoff_max=cutoff_max,
            # exclude_output_signals=False,
        )
        # pprint.pprint(ret)

        p += [ ret['p'] ]
        snk += [ sink_delay ]
        src += [ source_delay ]

        plotting.plot(
          times,
          states,
          list(init.keys()),
          fname=f"{sink_delay}-{source_delay}.svg",
          susceptible=ret['susceptible'],
          cutoff=[cutoff_min, cutoff_max],
          )

    with open('p_sweepink_snk_src.pickle', 'wb') as f:
        print('[info] saving data to pickle')
        pickle.dump({
            'p': p,
            'snk': snk,
            'src':src},
            f)



# # plot the last one
# plotting.plot(
#   times,
#   states,
#   list(init.keys()),
#   susceptible=ret['susceptible'],
#   cutoff=[cutoff_min, cutoff_max],
#   )

with open('p_sweepink_snk_src.pickle', 'rb') as f:
    print('[info] loaded data from pickle')
    loaded_obj = pickle.load(f)

snk = np.array(loaded_obj['snk'])
src = np.array(loaded_obj['src'])
p = np.array(loaded_obj['p'])

# plt.figure()
# ax = plt.axes(projection='3d')

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('sink delay [INV delay]')
ax.set_ylabel('source delay [INV delay]')
ax.invert_xaxis()
ax.invert_yaxis()
ax.set_zlabel('P(fail)')
ax.set_zlim(0,1)

# Shape 1 
#ax.plot3D(snk, src, p)

# Shape 2
# ax.scatter3D(snk, src, p, zdir='z',cmap='viridis')

# Shape 3
df = pd.DataFrame({'x': snk, 'y': src, 'z': p})

Xplot = np.reshape(list(df.x), (NUM, NUM))
Yplot = np.reshape(list(df.y), (NUM, NUM))
Zplot = np.reshape(list(df.z), (NUM, NUM))

#surf = ax.plot_wireframe(Xplot, Yplot, Zplot)
#ax.invert_yaxis()

norm = plt.Normalize(Zplot.min(), Zplot.max())
colors = cm.viridis(norm(Zplot))
rcount, ccount, _ = colors.shape
surf = ax.plot_surface(Xplot, Yplot, Zplot, rcount=rcount, ccount=ccount,
                       facecolors=colors, shade=False)
surf.set_facecolor((0,0,0,0))
ax.invert_xaxis()

fname = 'muller3_sweep_3dplot.png'
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
# plt.show()


