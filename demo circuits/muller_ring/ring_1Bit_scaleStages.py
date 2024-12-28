import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../../')

import pprint
from libs import tracem as tr
from libs import plotting
# from libs import checkbi as check
from depricated import check
from libs import preprocessing as p

CHECK = True 	# show sensitivity windows
# CHECK = False	# show effect of specific glitches

# fault = 'SET'
# fault = 'SA0'
# fault = 'SA1'
fault = 'SAF'

# CREATE RING w/ 1 BIT (not dual-rail) AND VARIABLE NUMBER OF STAGES

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
	print(f"D={data_t}, S={spacer_t}, B={bubbles}")

	# first tag each stage
	for i in range(0, num_stages):
		if bubbles >= 2*data_t and bubbles >= 2*spacer_t:
			tag[i] = 'B'
			bubbles -= 1
		# elif spacer_t > data_t:
		#     tag[i] = 'S'
		#     spacer_t -= 1
		# else:
		#     tag[i] = 'D'
		#     data_t -= 1
		elif data_t > spacer_t:
			tag[i] = 'D'
			data_t -= 1
		else:
			tag[i] = 'S'
			spacer_t -= 1
		

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
			for s in signals:
						if str(stage) in s:
							# if ('en' in s):
							#     init[s] = 0
							# if ('c' in s):
							#     init[s] = 1
							if ('en' in s):
								init[s] = 1
							if ('c' in s):
								init[s] = 0
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

	for x in init:
		print(x, init[x])

	return init

# ----------------------------------------------------------------------------------------------------------

# run it

num_stages = 5
num_tokens = 4
T = 100

# create it
signals, output_signals = createCircuit(num_stages=num_stages)

# initialize it
init = initCircuit(num_stages=num_stages, num_tokens=num_tokens, signals=signals)

events = []

if not CHECK:
	if fault == 'SET':
		benign_glitch1 = 3.9
		nasty_glitch1 = 4.5
		nasty_glitch2 = 15.5
		nasty_glitch3 = 9.5
		events += [
			# benign glitch 1
			# (benign_glitch1, 'c2', 1),  # add glitch
			# (benign_glitch1 + 0.1, 'c2', 0),  # reset glitch

			# # nasty glitch 1
			(nasty_glitch1, 'c2', 1),  # add glitch
			(nasty_glitch1 + 0.1, 'c2', 0),  # reset glitch

			# nasty glitch 2
			# (nasty_glitch2, 'c2', 1),  # add glitch
			# (nasty_glitch2 + 0.1, 'c2', 0),  # reset glitch

			# nasty glitch 3
			# (nasty_glitch3, 'c3', 0),  # add glitch
			# (nasty_glitch3 + 0.1, 'c3', 1),  # reset glitch
		]

		times, states = tr.trace(init, events=events, T=T)

	elif fault == 'SA1':
		stuck_sig = 'en1'
		stuck_value = 1
		stuck_t = 54.1
		events += [
				(stuck_t, stuck_sig, stuck_value),  # add SA1 
		]

		# checking that it will stay stuck
		events += [(stuck_t, stuck_sig, not stuck_value)]
		events += [(stuck_t+10, stuck_sig, not stuck_value)]

		times, states = tr.traceSA(init, events, stuck_sig, stuck_value, stuck_t, T=T)

	else:
		stuck_sig = 'en1'
		stuck_value = 0
		stuck_t = 36.1
		events += [
				(stuck_t, stuck_sig, stuck_value),  # add SA1 
		]

		# checking that it will stay stuck
		events += [(stuck_t, stuck_sig, not stuck_value)]
		events += [(stuck_t+10, stuck_sig, not stuck_value)]

		times, states = tr.traceSA(init, events, stuck_sig, stuck_value, stuck_t, T=T)

# if CHECK, run golden run without any faults
else:
	times, states = tr.trace(init, events, output_signals, T=T)

plotting.plot(times, states, init.keys())

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])

# cutoff
cutoff_min = 0
cutoff_max = float('Inf')

if CHECK:
	if fault == 'SET':
		ret = check.check(
				times=times,
				events=events,
				states=states,
				signals=list(init.keys()),
				output_signals=output_signals,
				cutoff_min=cutoff_min,
				cutoff_max=cutoff_max,
		)
		pprint.pprint(ret)

		plotting.plot(
				times,
				states,
				list(init.keys()),
				susceptible=ret['susceptible'],
				cutoff=[cutoff_min, cutoff_max],
				)
	else:
		# ret = check.checkSA(
		# 	times=times,
		# 	events=events,
		# 	states=states,
		# 	signals=list(init.keys()),
		# 	output_signals=output_signals, 
		# 	cutoff_min=cutoff_min,
		# 	cutoff_max=cutoff_max,
		# 	fault=fault,
		# )
		# pprint.pprint(ret)

		# susceptible_SA = p.appendSAF(p.collapseRanges(ret['susceptible'] if ret else []), fault)

		# plotting.plot(
		# 	times,
		# 	states,
		# 	list(init.keys()),
		# 	# susceptible=ret['susceptible'],
		# 	susceptible=susceptible_SA,
		# 	fault=fault,
		# 	cutoff=[cutoff_min, cutoff_max],
		# 	)
		

		SA1_M = {}
		SA0_M = {}

		if fault == 'SAF' or fault == 'SA1':
			SA1_M = check.checkSA(
				times=times,
				states=states,
				events=events,
				signals=list(init.keys()),
				output_signals=output_signals, 
				cutoff_min=cutoff_min,
				cutoff_max=cutoff_max,
				fault='SA1',
				# victim_signals=[]
			)
			pprint.pprint(SA1_M)

		if fault == 'SAF' or fault == 'SA0':
			SA0_M = check.checkSA(
				times=times,
				states=states,
				events=events,
				signals=list(init.keys()),
				output_signals=output_signals, 
				cutoff_min=cutoff_min,
				cutoff_max=cutoff_max,
				fault='SA0',
				# victim_signals=[]
			)
			pprint.pprint(SA0_M)

		susceptible_SA1 = p.appendSAF(p.collapseRanges(SA1_M['susceptible'] if SA1_M else []), 'SA1')
		susceptible_SA0 = p.appendSAF(p.collapseRanges(SA0_M['susceptible']if SA0_M else []), 'SA0')

		susceptible = susceptible_SA1 + susceptible_SA0

		plotting.plot(
			times,
			states,
			list(init.keys()),
			susceptible=susceptible,
			fault=fault,
			cutoff=[cutoff_min, cutoff_max],
			)

