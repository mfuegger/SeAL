import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../../')

import pprint
from libs import tracem as tr
from libs import plotting
from libs import check
import math as m
import numpy as np
import matplotlib.pyplot as plt

# circuit (at least 3 stages)
# Muller Pipeline (ring)

def createCircuit(num_stages, delay):

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
            tr.rise(f=tr.Cr, i=[f'c{num_stages}', f'en{i}'], o=f'c{i}', d=delay)
            tr.fall(f=tr.Cf, i=[f'c{num_stages}', f'en{i}'], o=f'c{i}', d=delay)
        else:
            tr.rise(f=tr.Cr, i=[f'c{i-1}', f'en{i}'], o=f'c{i}', d=delay)
            tr.fall(f=tr.Cf, i=[f'c{i-1}', f'en{i}'], o=f'c{i}', d=delay) 

        signals.append(f'en{i}')
        signals.append(f'c{i}')

    return signals, output_signals

# ----------------------------------------------------------------------------------------------------------

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
        if bubbles >= data_t and bubbles >= spacer_t:
        # spread bubbles
        # if bubbles >= 2*data_t and bubbles >= 2*spacer_t:
            tag[i] = 'B'
            bubbles -= 1

        # place D before S
        # elif spacer_t > data_t:
        #     tag[i] = 'S'
        #     spacer_t -= 1
        # else:
        #     tag[i] = 'D'
        #     data_t -= 1

        # place S before D
        elif data_t > spacer_t:
            tag[i] = 'D'
            data_t -= 1
        else:
            tag[i] = 'S'
            spacer_t -= 1

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
                    # Bd
                    # if ('en' in s):
                    #     init[s] = 0
                    # if ('c' in s):
                    #     init[s] = 1

                    # Bs
                    if ('en' in s):
                        init[s] = 1
                    if ('c' in s):
                        init[s] = 0


        stage += 1  

#     for x in init:
#         print(x, init[x])

    return init

# ----------------------------------------------------------------------------------------------------------

# run it

tokens = 2
stages = 10
delay = 10
p = []

plt.figure()
sweep_values = []
# labels = []
# markers = []

# checking for 110 tokens
for d in range(1, delay+1):
    print(f'[info] computing for delay {d}')

    sweep_values += [d]
    
    # clear circuit
    tr.clear()
        
    # create it
    signals, output_signals = createCircuit(num_stages=stages, delay=d)

    # initialize it
    init = initCircuit(num_stages=stages, num_tokens=tokens, signals=signals)

    # trace it
    T = 100
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

    p += [ret['p']]
    # pprint.pprint(sweep_values)
    # pprint.pprint(p)

plt.plot(sweep_values, p, linestyle='-', marker='o')

plt.xlabel('C gate delay')
plt.ylabel('P(fail)')
plt.xlim(1, delay)
plt.ylim(0, 1)
# plt.legend(loc=3)
plt.title(f"{tokens} token(s) / {stages} stages")

fname = f'muller-ring-sweepDelay-{tokens}per{stages}.png'
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
