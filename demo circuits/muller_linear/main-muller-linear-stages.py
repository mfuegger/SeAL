import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../../')

import pprint
from libs import tracem as tr
from libs import plotting
from libs import checkbi as check
import math as m

CHECK = True

# circuit (at least 3 stages)
# Muller Pipeline (linear)

num_stages = 5
source_delay = 4
sink_delay = 4

output_signals = ['c1', f'c{num_stages}']

signals = ['c_in']

#  max number of tokens (of each kind DATA/SPACER)
#  based on the number of stages
max_tokens = m.floor((num_stages-1)/2)

# DATA & SPACER, num_tokens of each
# num_tokens = 1

# c_in
tr.rise(f=tr.INVr, i=['c1'], o='c_in', d=source_delay)
tr.fall(f=tr.INVf, i=['c1'], o='c_in', d=source_delay)

for i in range(1, num_stages+1):
    if i == num_stages:
        # ack_in
        tr.rise(f=tr.INVr, i=[f'c{i}'], o=f'en{i}', d=sink_delay)
        tr.fall(f=tr.INVf, i=[f'c{i}'], o=f'en{i}', d=sink_delay)
    else:    
        # en
        tr.rise(f=tr.INVr, i=[f'c{i+1}'], o=f'en{i}', d=1)
        tr.fall(f=tr.INVf, i=[f'c{i+1}'], o=f'en{i}', d=1)

    # c
    if i == 1:
        tr.rise(f=tr.Cr, i=['c_in', f'en{i}'], o=f'c{i}', d=5)
        tr.fall(f=tr.Cf, i=['c_in', f'en{i}'], o=f'c{i}', d=5)
    else:
        tr.rise(f=tr.Cr, i=[f'c{i-1}', f'en{i}'], o=f'c{i}', d=5)
        tr.fall(f=tr.Cf, i=[f'c{i-1}', f'en{i}'], o=f'c{i}', d=5) 

    signals.append(f'en{i}')
    signals.append(f'c{i}')


# pprint.pprint(rules)
# pprint.pprint(signals)

# run it

init = {}
for s in signals:
    if ('en' in s):
        init[s] = 1
    if ('c' in s):
        init[s] = 0

events = []

if not CHECK:
    benign_glitch1 = 22.9
    nasty_glitch1 = 23
    events += [
        # benign glitch
        # (benign_glitch1, 'c2', 0),  # add glitch
        # (benign_glitch1 + 0.1, 'c2', 1),  # reset glitch

        # nasty glitch
        (nasty_glitch1, 'c2', 0),  # add glitch
        (nasty_glitch1 + 0.1, 'c2', 1),  # reset glitch
    ]

times, states = tr.trace(init, events=events, T=32)

plotting.plot(times, states, signals)

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])

# cutoff
cutoff_min = 0
cutoff_max = float('Inf')

if CHECK:
    ret = check.check(
            times=times,
            events=events,
            states=states,
            signals=signals,
            output_signals=output_signals,
            cutoff_min=cutoff_min,
            cutoff_max=cutoff_max
    )
    # pprint.pprint(ret)

    plotting.plot(
            times,
            states,
            signals,
            susceptible=ret['susceptible'],
            cutoff=[cutoff_min, cutoff_max],
            )

