import trace as tr

def check(times, states, signals, output_signals, Mdelta=0.1, Textra=30):
	susceptible_intervals = []
	pos = 0
	neg = 0
	T = times[-1] + Textra

	non_output_signals = [ s for s in signals if s not in output_signals ]
	for s in non_output_signals:
		for i in range(len(times)-1):
			t = times[i]
			events = [
				(t,          s, 0.5),           # add glitch
    			(t + Mdelta, s, states[i][s]),  # reset glitch
			]
			times_M, states_M = tr.trace(states[0], events=events, T=T, verbose=False)
			
			was_M = False
			for state_M in states_M:
				was_M = was_M or any([ state_M[s] == 0.5 for s in output_signals ])
			
			if was_M:
				susceptible_intervals += [ (s, [times[i], times[i+1]]) ]
				pos += times[i+1] - times[i]
			else:
				neg += times[i+1] - times[i]

	return {
		'p': pos/(pos+neg),
		'susceptible': susceptible_intervals
	}
