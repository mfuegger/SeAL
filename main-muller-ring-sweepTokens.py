import pprint
import tracem as tr
import plotting
import checkbi as check
import math as m
import numpy as np
import matplotlib.pyplot as plt

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

    pprint.pprint(tag)

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
        # else:
        #     # bubble is of the same type as the subsequent non-bubble stage
        #     for ts in range(stage-1, num_stages-1):
        #         if tag[ts+1] == 'B':
        #             # temp_stage += 1
        #             continue
        #         elif tag[ts+1] == 'D':
        #             for s in signals:
        #                 if str(stage) in s:
        #                     if ('en' in s):
        #                         init[s] = 0
        #                     if ('c' in s):
        #                         init[s] = 1
        #             break
        #         elif tag[ts+1] == 'S':
        #             for s in signals:
        #                 if str(stage) in s:
        #                     if ('en' in s):
        #                         init[s] = 1
        #                     if ('c' in s):
        #                         init[s] = 0
        #             break

        stage += 1  

#     for x in init:
#         print(x, init[x])

    return init

# ----------------------------------------------------------------------------------------------------------

# run it

tokens = 6   # 6
stages = 20  # 20
results = {}

plt.figure()
labels = []
markers = []

# checking for 1-4 tokens
for t in range(1, tokens+1):
    
    labels.append(f'{t} token(s)')

    # min number of stages for t tokens
    min_stages = 2*t+1

    results[t] = {'stages':[], 'p':[]}

    for s in range(min_stages, stages+1):
        print(f'[info] computing {t} tokens / {s} stages')

        # clear circuit
        tr.clear()
        
        # create it
        signals, output_signals = createCircuit(num_stages=s)

        # initialize it
        init = initCircuit(num_stages=s, num_tokens=t, signals=signals)

        # trace it
        T = 500
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

        results[t]['stages'] += [s]
        results[t]['p'] += [ret['p']]
        # print(f"Stages = {s} & Tokens = {t}")
        # pprint.pprint(results)
        # pprint.pprint(ret)

    plt.plot(results[t]['stages'], results[t]['p'], linestyle='-', marker='o', label=labels[t-1])

plt.xlabel('#stages')
plt.ylabel('P(fail)')
plt.xlim(3-0.3, stages+0.3)
plt.xticks(np.arange(3, stages+1, step=1))
plt.ylim(0, 1)
plt.legend(loc=3)

fname = f'muller-ring-sweepTokens.png'
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
