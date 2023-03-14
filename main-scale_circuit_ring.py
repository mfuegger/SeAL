import pprint
import tracem as tr
import plotting
import checkbi as check
import numpy as np
import math as m

# ---- testing ------

# circuit (at least 3 stages/2 bits)
# 2 dual-rail bit linear pipeline

num_stages = 3
num_bits = 4

a = np.array(num_bits)
b = np.array(num_bits)

steps = int(m.log2(num_bits))

c_dict = {}
for c in range(steps):
    c_dict[f'list{c+1}'] = []

output_signals = ['ack1']
for j in range(num_bits):
    output_signals.append(f'ca{num_stages}F[{j}]')
    output_signals.append(f'ca{num_stages}T[{j}]')
    output_signals.append(f'cb{num_stages}F[{j}]')
    output_signals.append(f'cb{num_stages}T[{j}]')

signals = []
for i in range(1, num_stages+1):
    signals.append(f'en{i}')
    signals.append(f'c{i}')

# print("Output Signals")
# for i in range(len(output_signals)):
#     print(output_signals[i])
    

# Start circuit

for i in range(1, num_stages+1):
    # Last stage (ackin)     
    if (i == num_stages):
        tr.rise(f=tr.INVr, i=[f'ack{1}'], o=f'en{i}', d=1)
        tr.fall(f=tr.INVf, i=[f'ack{1}'], o=f'en{i}', d=1)

    else:
	# inv_2                 ack3        en2
        tr.rise(f=tr.INVr, i=[f'ack{i+1}'], o=f'en{i}', d=1)
        tr.fall(f=tr.INVf, i=[f'ack{i+1}'], o=f'en{i}', d=1)
        
        
    for j in range(num_bits):
        # First stage (inputs aF, aT, bF & bT)
        if (i == 1):
            # c_a1F[0]
            tr.rise(f=tr.Cr, i=[f'ca{num_stages}T[{j}]', f'en{i}'], o=f'ca{i}F[{j}]', d=5)
            tr.fall(f=tr.Cf, i=[f'ca{num_stages}T[{j}]', f'en{i}'], o=f'ca{i}F[{j}]', d=5)

            # c_a1T[0]
            tr.rise(f=tr.Cr, i=[f'ca{num_stages}F[{j}]', f'en{i}'], o=f'ca{i}T[{j}]', d=5)
            tr.fall(f=tr.Cf, i=[f'ca{num_stages}F[{j}]', f'en{i}'], o=f'ca{i}T[{j}]', d=5)
            
            
            # c_b1F[0]
            tr.rise(f=tr.Cr, i=[f'cb{num_stages}T[{j}]', f'en{i}'], o=f'cb{i}F[{j}]', d=5)
            tr.fall(f=tr.Cf, i=[f'cb{num_stages}T[{j}]', f'en{i}'], o=f'cb{i}F[{j}]', d=5)

            # c_b1T[0]
            tr.rise(f=tr.Cr, i=[f'cb{num_stages}F[{j}]', f'en{i}'], o=f'cb{i}T[{j}]', d=5)
            tr.fall(f=tr.Cf, i=[f'cb{num_stages}F[{j}]', f'en{i}'], o=f'cb{i}T[{j}]', d=5)

        # Intermediate stages (input of stage is ouput of previous one)
        else:
            # c_a2F[0]                  ca1F[0]     en2            ca2F[0]
            tr.rise(f=tr.Cr, i=[f'ca{i-1}F[{j}]', f'en{i}'], o=f'ca{i}F[{j}]', d=5)
            tr.fall(f=tr.Cf, i=[f'ca{i-1}F[{j}]', f'en{i}'], o=f'ca{i}F[{j}]', d=5)

            # c_a2T[0]                 ca1T[0]      en2            ca2T[0] 
            tr.rise(f=tr.Cr, i=[f'ca{i-1}T[{j}]', f'en{i}'], o=f'ca{i}T[{j}]', d=5)
            tr.fall(f=tr.Cf, i=[f'ca{i-1}T[{j}]', f'en{i}'], o=f'ca{i}T[{j}]', d=5)


            # c_b2F[0]              cb1F[0]         en2             cb2F[0]
            tr.rise(f=tr.Cr, i=[f'cb{i-1}F[{j}]', f'en{i}'], o=f'cb{i}F[{j}]', d=5)
            tr.fall(f=tr.Cf, i=[f'cb{i-1}F[{j}]', f'en{i}'], o=f'cb{i}F[{j}]', d=5)

            # c_b2T[0]              cb1T[0]         en2             cb2T[0]
            tr.rise(f=tr.Cr, i=[f'cb{i}F[{j}]', f'en{i}'], o=f'cb{i}T[{j}]', d=5)
            tr.fall(f=tr.Cf, i=[f'cb{i}F[{j}]', f'en{i}'], o=f'cb{i}T[{j}]', d=5)
        
        # OR gate per bit for completion detection
        # or_a20                 ca2F[0]         ca2T[0]         ora21
        tr.rise(f=tr.ORr, i=[f'ca{i}F[{j}]', f'ca{i}T[{j}]'], o=f'ora{i}{j}', d=4)
        tr.fall(f=tr.ORf, i=[f'ca{i}F[{j}]', f'ca{i}T[{j}]'], o=f'ora{i}{j}', d=4)

        # or_b20                 cb2F[0]         cb2T[0]         orb20
        tr.rise(f=tr.ORr, i=[f'cb{i}F[{j}]', f'cb{i}T[{j}]'], o=f'orb{i}{j}', d=4)
        tr.fall(f=tr.ORf, i=[f'cb{i}F[{j}]', f'cb{i}T[{j}]'], o=f'orb{i}{j}', d=4)

        # MCE to check when both inputs belong to the same context
        # c_or21            ora20           orb20           cor20
        tr.rise(f=tr.Cr, i=[f'ora{i}{j}', f'orb{i}{j}'], o=f'cor{i}{j}', d=5)
        tr.fall(f=tr.Cf, i=[f'ora{i}{j}', f'orb{i}{j}'], o=f'cor{i}{j}', d=5)
        
        c_dict['list1'].append(f'cor{i}{j}')


    for c in range(steps):
        # Last MCE to join/merge all other MCEs (last step)
        if (c+1 == steps):
            # DEBUG
            # for c in range(3):
            #     print(c_dict.keys())
            #     print(f'list{steps}')
            #     print(len(c_dict[f'list{c+1}']))
            #     print(c_dict[f'list{steps}'])

            # First Stage (ackout)     
            if (i == 1):
                tr.rise(f=tr.Cr, i=[str(c_dict[f'list{steps}'][0]), str(c_dict[f'list{steps}'][1])], o=f'ack{i}', d=5)
                tr.fall(f=tr.Cf, i=[str(c_dict[f'list{steps}'][0]), str(c_dict[f'list{steps}'][1])], o=f'ack{i}', d=5)
            # All other stages (ack_i)     
            else:
                # ack2				c_dict[list1[0]]
                tr.rise(f=tr.Cr, i=[str(c_dict[f'list{steps}'][0]), str(c_dict[f'list{steps}'][1])], o=f'ack{i}', d=5)
                tr.fall(f=tr.Cf, i=[str(c_dict[f'list{steps}'][0]), str(c_dict[f'list{steps}'][1])], o=f'ack{i}', d=5)
        # Intermediate MCEs (intermediate steps)
        else:
            # which MCE we are creating
	    # iterate over the elements of the list in 2s
            for index in range(0, len(c_dict[f'list{c+1}']), 2):
                tr.rise(f=tr.Cr, i=[str(c_dict[f'list{c+1}'][index]), str(c_dict[f'list{c+1}'][index+1])], o=f"{'c'*(c+2)}{i}{index}", d=5)
                tr.fall(f=tr.Cf, i=[str(c_dict[f'list{c+1}'][index]), str(c_dict[f'list{c+1}'][index+1])], o=f"{'c'*(c+2)}{i}{index}", d=5)
                
                c_dict[f'list{c+2}'].append(f"{'c'*(c+2)}{i}{index}")

                # for cc in range(num_bits/pow(2, c+1)):
                # # c_ackout        cor10           cor11           cc1
                # tr.rise(f=tr.Cr, i=[f'cor1{c}', f'cor1{c+1}'], o=f'cc{c+1}', d=5)
                # tr.fall(f=tr.Cf, i=[f'cor1{c}', f'cor1{c+1}'], o=f'cc{c+1}', d=5)

    # Clear lists for new stage 
    for c in range(steps):
        c_dict[f'list{c+1}'].clear()

#######################################################
# pprint.pprint(rules)
# pprint.pprint(signals)

# run it
T = 400

init = {
    'en1': 1,   
    'ca1F[0]': 0,
    'ca1T[0]': 0,
    'ora10': 0,
    'ca1F[1]': 0,
    'ca1T[1]': 0,
    'ora11': 0,
    'cor10': 0,
    'cb1F[0]': 0,
    'cb1T[0]': 0,
    'orb10': 0,
    'cb1F[1]': 0,
    'cb1T[1]': 0,
    'orb11': 0,
    'cor11': 0,
    'ack1': 0,


    'en2': 0,
    'ca2F[0]': 0,
    'ca2T[0]': 0,
    'ora20': 0,
    'ca2F[1]': 0,
    'ca2T[1]': 0,
    'ora21': 0,
    'cor20': 0,
    'cb2F[0]': 0,
    'cb2T[0]': 0,
    'orb20': 0,
    'cb2F[1]': 0,
    'cb2T[1]': 0,
    'orb21': 0,
    'cor21': 0,
    'ack2': 0,

 
    'en3': 1,
    'ca3F[0]': 1,
    'ca3T[0]': 0,
    'ora30': 1,
    'ca3F[1]': 0,
    'ca3T[1]': 1,
    'ora31': 1,
    'cor30': 1,
    'cb3F[0]': 1,
    'cb3T[0]': 0,
    'orb30': 1,
    'cb3F[1]': 0,
    'cb3T[1]': 1,
    'orb31': 1,
    'cor31': 1,
    'ack3': 1,

    # Uncomment for 4 bits
    'ca1F[2]': 0,
    'ca1T[2]': 0,
    'ora12': 0,
    'ca1F[3]': 0,
    'ca1T[3]': 0,
    'ora13': 0,
    'cor12': 0,
    'cb1F[2]': 0,
    'cb1T[2]': 0,
    'orb12': 0,
    'cb1F[3]': 0,
    'cb1T[3]': 0,
    'orb13': 0,
    'cor13': 0,
    'cc10': 0,
    'cc12': 0,

    'ca2F[2]': 0,
    'ca2T[2]': 0,
    'ora22': 0,
    'ca2F[3]': 0,
    'ca2T[3]': 0,
    'ora23': 0,
    'cor22': 0,
    'cb2F[2]': 0,
    'cb2T[2]': 0,
    'orb22': 0,
    'cb2F[3]': 0,
    'cb2T[3]': 0,
    'orb23': 0,
    'cor23': 0,
    'cc20': 0,
    'cc22': 0,

    'ca3F[2]': 1,
    'ca3T[2]': 0,
    'ora32': 1,
    'ca3F[3]': 0,
    'ca3T[3]': 1,
    'ora33': 1,
    'cor32': 1,
    'cb3F[2]': 0,
    'cb3T[2]': 1,
    'orb32': 1,
    'cb3F[3]': 1,
    'cb3T[3]': 0,
    'orb33': 1,
    'cor33': 1,
    'cc30': 1,
    'cc32': 1,

}

glitch_t = 4
events = [
	# (5, 'aF', 0),
	# (10, 'bF', 0),
	# (44, 'ackin', 0),
	# (50, 'aT', 1),
    # (55, 'bT', 1),
	# (10, 'a', 1),
    # (glitch_t, 'c3', .5),  # add glitch
    # (glitch_t + 0.1, 'c3', 0),  # reset glitch
]
times, states = tr.trace(init, events=events, T=T)

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])
        
ret = check.check(times=times, events=events, states=states, signals=list(init.keys()), output_signals=output_signals)
pprint.pprint(ret)

plotting.plot(times, states, list(init.keys()), susceptible=ret['susceptible'])

