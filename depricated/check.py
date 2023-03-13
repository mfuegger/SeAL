import tracem as tr

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
				# region overlaps with cropped region
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
