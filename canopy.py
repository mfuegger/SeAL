import pprint
import tracem as tr
import plotting
import checkbi as check
import math as m
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.parasite_axes import HostAxes


# circuit (at least 3 stages)
# Muller Pipeline (ring)

def createCircuit(num_stages):

    signals = []
    output_signals = ['c1', f'c{num_stages}']

    for i in range(1, num_stages+1):
        #  Last stage
        if i == num_stages:
            # ack_in
            tr.rise(f=tr.INVr, i=['c1'], o=f'en{i}', d=1)
            tr.fall(f=tr.INVf, i=['c1'], o=f'en{i}', d=1)
        else:    
            # en
            tr.rise(f=tr.INVr, i=[f'c{i+1}'], o=f'en{i}', d=1)
            tr.fall(f=tr.INVf, i=[f'c{i+1}'], o=f'en{i}', d=1)

        # c
        #  First stage
        if i == 1:
            tr.rise(f=tr.Cr, i=[f'c{num_stages}', f'en{i}'], o=f'c{i}', d=5)
            tr.fall(f=tr.Cf, i=[f'c{num_stages}', f'en{i}'], o=f'c{i}', d=5)
        else:
            tr.rise(f=tr.Cr, i=[f'c{i-1}', f'en{i}'], o=f'c{i}', d=5)
            tr.fall(f=tr.Cf, i=[f'c{i-1}', f'en{i}'], o=f'c{i}', d=5) 

        signals.append(f'en{i}')
        signals.append(f'c{i}')

    return signals, output_signals

# ----------------------------------------------------------------------------------------------------------

def getThroughput(times, states, signal='c1'):
    # measures 0->1 transitions / time
    transition_0to1 = [ 1 for i in range(len(states)-1) if states[i][signal] == 0 and states[i+1][signal] == 1 ]
    return len(transition_0to1) / (times[-1] - times[0])


def initCircuit(num_stages, num_tokens, signals):  
    # for initilazing the circuit
    # always starts either with a DATA token or a bubble
    # will never initialize the last stage with a bubble
    tag = [None] * num_stages
    init = {}
    # print(f"length of tag list = {len(tag)}")

    # initialize circuit
    data_t = spacer_t = num_tokens
    bubbles = num_stages - data_t - spacer_t

    # first tag each stage
    for i in range(0, num_stages):
        # bubbles at the beginning
        # if bubbles >= data_t and bubbles >= spacer_t:
        # spread bubbles
        if bubbles >= 2*data_t and bubbles >= 2*spacer_t:
            tag[i] = 'B'
            bubbles -= 1

        # place D before S
        elif spacer_t > data_t:
            tag[i] = 'S'
            spacer_t -= 1
        else:
            tag[i] = 'D'
            data_t -= 1

        # place S before D
        # elif data_t > spacer_t:
        #     tag[i] = 'D'
        #     data_t -= 1
        # else:
        #     tag[i] = 'S'
        #     spacer_t -= 1

#     pprint.pprint(tag)

    # then populate the init{}
    stage = 1
    for t in tag:
        if t == 'D':
            for s in signals:
                if str(stage) in s:
                    if ('en' in s):
                        init[s] = 1
                    if ('c' in s):
                        init[s] = 1
        elif t == 'S':
            for s in signals:
                if str(stage) in s:
                    if ('en' in s):
                        init[s] = 0
                    if ('c' in s):
                        init[s] = 0
        else:
            # depending on D or S first,
            # B should be Bd or Bs
            for s in signals:
                if str(stage) in s:
                    # Bd coz D first
                    if ('en' in s):
                        init[s] = 0
                    if ('c' in s):
                        init[s] = 1

                    # Bs coz S first
                    # if ('en' in s):
                    #     init[s] = 1
                    # if ('c' in s):
                    #     init[s] = 0

        stage += 1  

#     for x in init:
#         print(x, init[x])

    return init

# ----------------------------------------------------------------------------------------------------------

# run it

tokens = 6   # 6
stages = 20  # 20
p = []
throughput = []
T = 200

sweep_values = np.linspace(1, tokens, num=tokens)

# create circuit with stages
signals, output_signals = createCircuit(num_stages=stages)

# check P for different occupancy
for t in range(1, tokens+1):
    print(f'[info] computing {t} tokens')

    # initialize circuit
    init = initCircuit(num_stages=stages, num_tokens=t, signals=signals)

    # trace it
    events = []

    times, states = tr.trace(init, events=events, T=T)

    # check it
    # cutoff
    cutoff_min = 0
    cutoff_max = float('Inf')

    ret = check.check(
        times=times,
        events=events,
        states=states,
        signals=signals,
        output_signals=output_signals,
        cutoff_min=cutoff_min,
        cutoff_max=cutoff_max
    )

    p += [ ret['p'] ]
    throughput += [ getThroughput(times, states, signal='c1') ]
    print(p)
    print(throughput)


# fig = plt.figure()

# host = fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes)
# par1 = host.twinx()

# host.axis["right"].set_visible(False)

# par1.axis["right"].set_visible(True)
# par1.axis["right"].major_ticklabels.set_visible(True)
# par1.axis["right"].label.set_visible(True)

# p1, = host.plot([0, 1, 2], [0, 1, 2], label="P(fail)")
# p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Performance")

# host.set(xlim=(1-0.3, tokens+0.3), ylim=(0, 1), xlabel="#tokens", ylabel="P(fail)")
# par1.set(ylim=(0, 1), ylabel="Performance")
# host.legend()

# host.axis["left"].label.set_color(p1.get_color())
# par1.axis["right"].label.set_color(p2.get_color())

# host.axis["left"].label.set_color(p1.get_color())
# par1.axis["right"].label.set_color(p2.get_color())  

x = sweep_values
y1 = p
# y2 = [2, 4, 3, 1]
y2 = throughput  # [0.04, 0.08, 0.06, 0.02]

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(x, y1, 'g-o')
ax2.plot(x, y2, 'b-o')

ax1.set_xlabel('#tokens')
ax1.set_xlim(1-0.3, tokens+0.3)
ax1.set_xticks(np.arange(1, tokens+1, step=1))
ax1.set_ylabel('P(fail)', color='g')
ax1.set_ylim(0, 1)
ax2.set_ylabel('Throughput [1 / INV delay]', color='b')
ax2.set_ylim(0, 0.1)

# plt.plot(sweep_values, p, linestyle='-', marker='o')
# plt.xlabel('#tokens')
# plt.ylabel('P(fail)')
# plt.xlim(1-0.3, tokens+0.3)
# plt.xticks(np.arange(1, tokens+1, step=1))
# plt.ylim(0, 1)
# plt.legend(loc=3)
plt.show()

fname = 'canopy.png'
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