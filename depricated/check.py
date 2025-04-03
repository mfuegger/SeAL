import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
sys.path.append(dir_path + '/../')

import numpy as np

from libs import tracem as tr

def check(times, states, events, signals, output_signals, Mdelta=0.1, Textra=30, MafterGrid=0.01, cutoff_min=5, cutoff_max=float('Inf')):

	susceptible_intervals = []
	pos = 0
	neg = 0
	T = times[-1] + Textra

	non_output_signals = [ s for s in signals if s not in output_signals ]
	for s in non_output_signals:
		for i in range(len(times)-1):
			t = times[i]
			events_check = events + [
				(t + MafterGrid,          s, 0.5),           # add glitch
    			(t + MafterGrid + Mdelta, s, states[i][s]),  # reset glitch
			]
			times_M, states_M = tr.trace(states[0], events=events_check, T=T, verbose=False)
			
			was_M = False
			for state_M in states_M:
				was_M = was_M or any([ state_M[s] == 0.5 for s in output_signals ])
			
			if times[i] <= cutoff_max and times[i+1] >= cutoff_min:
				## region overlaps with cropped region
				t_from = max(cutoff_min, times[i])
				t_to =   min(cutoff_max, times[i+1])

				if was_M:
					susceptible_intervals += [ (s, [t_from, t_to]) ]
					pos += t_to - t_from
				else:
					neg += t_to - t_from

	return {
		'p': pos/(pos+neg) if pos + neg > 0 else 'undefined',
		'cutoff_min': cutoff_min,
		'cutoff_max': cutoff_max,
		'susceptible': susceptible_intervals
	}



def checkSA(times, states, events, signals, output_signals,
			Mdelta=0.1,
			Textra=30,
			MafterGrid=0.01,
			cutoff_min=5, cutoff_max=float('Inf'),
			exclude_output_signals=True,
			fault='SA0'):
	

	susceptible_intervals = []
	pos = 0
	neg = 0
	T = times[-1] + Textra

	if fault == 'SA0':
		SAF = 0
	elif fault == 'SA1':
		SAF = 1
	# else:
	# 	SA = None

	non_output_signals = [ s for s in signals if s not in output_signals ]

	for s in non_output_signals:
		# for i in range(len(injections)-1):
		j = 0
		for i in range(len(times)):
			# t = times[i]

			# for k in np.arange(0, t, 0.1):
			# 	print(k)
			# for k in np.arange(0, T, 0.1):
			# 	print("s = ", s)
			# 	print("states = ", states[t][s])
			# 	print("k = ", k)
			
			# if states[i][s] == '1':
			while j < times[i]:
			# while j <= times[i]:
				# events_check = events + [
				# 	(j,          s, SA),           # add SA0 or SA1
				# ]
				
				# times_M, states_M = tr.traceSA(states[0], events=events_check, SA_sig=s, SA_time=j, T=T, verbose=False)


				events_check = events + [
					(j + MafterGrid,          s, SAF),           # add SA0 or SA1
				]
				
				times_M, states_M = tr.traceSA(states[0], events_check, output_signals, SA_signal=s, SA_value=SAF, SA_time=j+MafterGrid, T=T, verbose=False)
				
				# Did X appear at any output signal at any of the circuit's states?
				was_M = False
				for state_M in states_M:
					was_M = was_M or any([ state_M[s] == 0.5 for s in output_signals ])
				
				# if times[i] <= cutoff_max and times[i+1] >= cutoff_min:
				# 	## region overlaps with cropped region
				# 	t_from = max(cutoff_min, j)
				# 	t_to =   min(cutoff_max, j+0.1)

				if was_M:
					susceptible_intervals += [ (s, [j, round(j+0.1, 1)]) ]
					# pos += t_to - t_from
					pos += 0.1
				else:
					# neg += t_to - t_from
					neg += 0.1
			
				j = round(j + 0.1, 1)

	for s in output_signals:
		# pos_per_sig[s] += times[-1] - times[0]

		if not exclude_output_signals:
			susceptible_intervals += [ (s, [times[0], times[-1]]) ]
			pos += times[-1] - times[0]


	return {
		'p': pos/(pos+neg) if pos + neg > 0 else 'undefined',
		'cutoff_min': cutoff_min,
		'cutoff_max': cutoff_max,
		'susceptible': susceptible_intervals
	}
