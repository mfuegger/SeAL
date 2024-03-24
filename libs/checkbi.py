from tqdm import tqdm

from libs import tracem as tr

ERROR = 0.001


def getStateAtTime(times, states, time: float):
	"""
	given the execution as <times> and <states>,
	returns the state vector at time <time>
	"""
	assert (time >= 0 and time <= times[-1]), "getStateAtTime: out of bounds time"

	for i, t in enumerate(times):
		if t > time:
			return states[i-1]

	return states[-1]


def isSusceptible(t, s, states, s_state, events, T, output_signals, MafterGrid=0.001, Mdelta=0.001, monitor=False, tokens=None, input_widths=None, output_widths=None):
	events_check = events + [
		(t + MafterGrid,          s, 0.5),      # add glitch
		(t + MafterGrid + Mdelta, s, s_state),  # reset glitch
	]
	# print((f"------------SA_signal {s} injected at time {t} ----------"))
	# print(f"\t\t\t init value = {states[0][s]}")
	# print(f"SET @ {s} @ {t}")
	# print(s_state)
	# changed
	times_M, states_M = tr.trace(states[0], events=events_check, output_signals=output_signals, T=T, verbose=False, monitor=monitor, tokens=tokens, input_widths=input_widths, output_widths=output_widths)

	was_M = False
	for state_M in states_M:
		was_M = was_M or any([ state_M[s] == 0.5 for s in output_signals ])

	return was_M


def findBoundary(tfrom, tto, s, states, s_state, events, T, output_signals, initially=True, monitor=False, tokens=None, input_widths=None, output_widths=None):
	# if initially:
	# 	print(tfrom, tto)

	# changed instead of what comes next changed (uncomment to go back)
	# ----------------------------------------------------------------------------------------------------------------------
	# # check if anywhere marked
	# if not isSusceptible(t=tto, s=s, states=states, s_state=s_state, events=events, T=T, output_signals=output_signals, MafterGrid=-0.05, monitor=True, tokens=tokens, input_widths=input_widths, output_widths=output_widths):
	# 	# no -> return boundary at end
	# 	return tto

	# # check if all marked (only initially)
	# elif initially and isSusceptible(t=tfrom, s=s, states=states, s_state=s_state, events=events, T=T, output_signals=output_signals, MafterGrid=0.001, monitor=True, tokens=tokens, input_widths=input_widths, output_widths=output_widths):
	# 	# yes -> return boundary at start
	# 	return tfrom
	# ----------------------------------------------------------------------------------------------------------------------
	
	# check if anywhere marked
	if not isSusceptible(t=tto, s=s, states=states, s_state=s_state, events=events, T=T, output_signals=output_signals, MafterGrid=-0.05, monitor=monitor, tokens=tokens, input_widths=input_widths, output_widths=output_widths):
		# no -> return boundary at end
		return tto

	# check if all marked (only initially)
	elif initially and isSusceptible(t=tfrom, s=s, states=states, s_state=s_state, events=events, T=T, output_signals=output_signals, MafterGrid=0.001, monitor=monitor, tokens=tokens, input_widths=input_widths, output_widths=output_widths):
		# yes -> return boundary at start
		return tfrom

	# else intersect
	else:
		middle = (tto + tfrom)/2

		if tto - tfrom <= 0.05:
			return middle
		
		# if tto - tfrom <= 0.01:
		# 	return round(middle, 2)

		else:
			middle_is_M = isSusceptible(t=middle, s=s, states=states, s_state=s_state, events=events, T=T, output_signals=output_signals, MafterGrid=0.001, monitor=monitor, tokens=tokens, input_widths=input_widths, output_widths=output_widths)

			if middle_is_M:
				# boundary must be on the left half
				return findBoundary(tfrom=tfrom, tto=middle, s=s, states=states, s_state=s_state, events=events, T=T, output_signals=output_signals, initially=False, monitor=monitor, tokens=tokens, input_widths=input_widths, output_widths=output_widths)

			else:
				# boundary must be on the right half
				return findBoundary(tfrom=middle, tto=tto, s=s, states=states, s_state=s_state, events=events, T=T, output_signals=output_signals, initially=False, monitor=True, tokens=tokens, input_widths=input_widths, output_widths=output_widths)

def check(times, states, events, signals, output_signals,
	Textra=30,
	exclude_output_signals=True,
	cutoff_min=0,
	cutoff_max=float('Inf'),
	monitor=False,
	tokens=None,
	input_widths=None,
	output_widths=None,
	victim_signals=[]
	):

	"""
	checking all equivalence regions
	"""
	susceptible_intervals = []
	pos = 0
	neg = 0
	pos_per_sig = { s: 0 for s in signals }
	T = times[-1] + Textra

	non_output_signals = [ s for s in signals if s not in output_signals ]

	if monitor:
		if tokens is None or input_widths is None or output_widths is None:
			raise Exception("Tokens and In/Output Widths missing!")

	# go over regions
	count=0	
	if len(victim_signals) != 0:
		# to test only a set of signals
		victims = tqdm(victim_signals, leave=True, desc="Victim Signals Progress")
		for s in v:
			victims.write("--------------------------------------------------")
			victims.write(f"SIGNAL {count} = {s}")
			victims.write("--------------------------------------------------")
			count+=1
			for i in range(len(times)-1):
				tfrom = times[i]
				tto = times[i+1]
				boundary = findBoundary(tfrom=tfrom, tto=tto, s=s, states=states, s_state=states[i][s], events=events, T=T, output_signals=output_signals, monitor=monitor, tokens=tokens, input_widths=input_widths, output_widths=output_widths)

				if boundary < tto:
					# it has a marked area:
					susceptible_intervals += [ (s, [boundary, tto]) ]
				
				assert (tto - boundary >= 0)
				assert (boundary - tfrom >= 0)

				pos += tto - boundary
				neg += boundary - tfrom

				pos_per_sig[s] += tto - boundary
				# print(pos_per_sig[s])

				# print(f"New susceptible = {tto - boundary}")
				# print(f"pos = {pos}")
				# print(f"New non-susceptible = {boundary - tfrom}")
				# print(f"neg = {neg}")
				# print(f"pos_per_sig[{s}] = {pos_per_sig[s]}")
				# print("--------------------------------------------------")
	
	else:
		# to test all signals in the circuit
		victims = tqdm(non_output_signals, leave=True, desc="Victim Signals Progress")
		for s in victims:
			victims.write("--------------------------------------------------")
			victims.write(f"SIGNAL {count} = {s}")
			victims.write("--------------------------------------------------")
			count+=1
			for i in range(len(times)-1):
				tfrom = times[i]
				tto = times[i+1]
				boundary = findBoundary(tfrom=tfrom, tto=tto, s=s, states=states, s_state=states[i][s], events=events, T=T, output_signals=output_signals, monitor=monitor, tokens=tokens, input_widths=input_widths, output_widths=output_widths)

				if boundary < tto:
					# it has a marked area:
					susceptible_intervals += [ (s, [boundary, tto]) ]
				
				assert (tto - boundary >= 0)
				assert (boundary - tfrom >= 0)

				pos += tto - boundary
				neg += boundary - tfrom
			
				pos_per_sig[s] += tto - boundary

				# print(f"New susceptible = {tto - boundary}")
				# print(f"pos = {pos}")
				# print(f"New non-susceptible = {boundary - tfrom}")
				# print(f"neg = {neg}")
				# print(f"pos_per_sig[{s}] = {pos_per_sig[s]}")
				# print("--------------------------------------------------")

	for s in output_signals:
		pos_per_sig[s] += times[-1] - times[0]

		if not exclude_output_signals:
			susceptible_intervals += [ (s, [times[0], times[-1]]) ]
			pos += times[-1] - times[0]

			# if times[i] <= cutoff_max and times[i+1] >= cutoff_min:
			#     # region overlaps with cropped region
			#     t_from = max(cutoff_min, times[i])
			#     t_to =   min(cutoff_max, times[i+1])

			#     if was_M:
			#         susceptible_intervals += [ (s, [t_from, t_to]) ]
			#         pos += t_to - t_from
			#     else:
			#         neg += t_to - t_from

	p = pos/(pos+neg) if pos + neg > 0 else 'undefined'
	p_per_sig = { s: pos_per_sig[s] / (times[-1] - times[0]) for s in signals }
	# print(p)
	# print(p_per_sig)

	assert (p <= 1)
	assert (p_per_sig[s] <= 1 for s in signals)

	return {
		'p': p,
		'p_per_sig': p_per_sig,
		'cutoff_min': cutoff_min,
		'cutoff_max': cutoff_max,
		'susceptible': susceptible_intervals
	}




def isSusceptibleSA(t, s, states, events, T, output_signals, SAF, MafterGrid): #MafterGrid=0.001
		
	events_check = events + [
		(t + MafterGrid, s, SAF),           # add SA0 or SA1
	]

	# print((f"SA_signal {s} stuck at {SAF} at time {t} "))
	# print(f"\t\t\t init value = {states[0][s]}")
	times_M, states_M = tr.traceSA(states[0], events_check, output_signals, SA_signal=s, SA_value=SAF, SA_time=t+MafterGrid, T=T, Mdelay=t+MafterGrid, verbose=False)
	
	was_M = False
	for state_M in states_M:
		was_M = was_M or any([ state_M[s] == 0.5 for s in output_signals ])	
	return was_M


def findBoundarySA(tfrom, tto, s, states, events, T, output_signals, SAF, start_is_M_initially, initially=True):
	# print(3*"*",tfrom,tto,initially)
	# if initially:
	# 	print(tfrom, tto)

	# global start_is_M_initially

	# if initially:
	# 	start_is_M_initially = isSusceptibleSA(t=tfrom, s=s, states=states, events=events, T=T, output_signals=output_signals, SAF=SAF, MafterGrid=0.001)

	# check if anywhere marked
	if initially:
		start_is_M = start_is_M_initially
	else:
		start_is_M = isSusceptibleSA(t=tfrom, s=s, states=states, events=events, T=T, output_signals=output_signals, SAF=SAF, MafterGrid=ERROR)
	
	end_is_M = isSusceptibleSA(t=tto, s=s, states=states, events=events, T=T, output_signals=output_signals, SAF=SAF, MafterGrid=-ERROR)

	if not start_is_M and not end_is_M:
		# no -> return boundary at end
		return tto

	# check if all marked (only initially)
	elif initially and start_is_M and end_is_M:
		# yes -> return boundary at start
		return tfrom

	# else intersect
	else:
		middle = (tto + tfrom)/2

		if tto - tfrom <= ERROR:
			return round(middle, 2)

		else:
			middle_is_M = isSusceptibleSA(t=middle, s=s, states=states, events=events, T=T, output_signals=output_signals, SAF=SAF, MafterGrid=ERROR)

			if middle_is_M:
				if not start_is_M_initially:
					# boundary must be on the left half
					return findBoundarySA(tfrom=tfrom, tto=middle, s=s, states=states, events=events, T=T, output_signals=output_signals, SAF=SAF, start_is_M_initially=start_is_M_initially, initially=False)
				else:
					# boundary must be on the right half
					return findBoundarySA(tfrom=middle, tto=tto, s=s, states=states, events=events, T=T, output_signals=output_signals, SAF=SAF, start_is_M_initially=start_is_M_initially, initially=False)
			else:
				if start_is_M_initially:
					# boundary must be on the left half
					return findBoundarySA(tfrom=tfrom, tto=middle, s=s, states=states, events=events, T=T, output_signals=output_signals, SAF=SAF, start_is_M_initially=start_is_M_initially, initially=False)
				else:
					# boundary must be on the right half
					return findBoundarySA(tfrom=middle, tto=tto, s=s, states=states, events=events, T=T, output_signals=output_signals, SAF=SAF, start_is_M_initially=start_is_M_initially, initially=False)


def checkSA(times, states, events, signals, output_signals,
	Textra=30,
	exclude_output_signals=True,
	cutoff_min=0, cutoff_max=float('Inf'),
	fault='SA0',
	victim_signals=[]):
	"""
	checking all equivalence regions
	"""
	susceptible_intervals = []
	pos = 0
	neg = 0
	pos_per_sig = { s: 0 for s in signals }
	T = times[-1] + Textra
	direction = 1

	if fault == 'SA0':
		SAF = 0
	elif fault == 'SA1':
		SAF = 1

	non_output_signals = [ s for s in signals if s not in output_signals ]

	count=0

	# go over regions
	if len(victim_signals) != 0:
		# to test only a set of signals
		victims = tqdm(victim_signals, leave=True, desc="Victim Signals Progress")
		for s in victims:
			victims.write("--------------------------------------------------")
			victims.write(f"SIGNAL {count} = {s}")
			victims.write("--------------------------------------------------")
			count+=1
			for i in range(len(times)-1):
				tfrom = times[i]
				tto = times[i+1]
				start_is_M_initially = isSusceptibleSA(t=tfrom, s=s, states=states, events=events, T=T, output_signals=output_signals, SAF=SAF, MafterGrid=ERROR)
				boundary = findBoundarySA(tfrom=tfrom, tto=tto, s=s, states=states, events=events, T=T, output_signals=output_signals, SAF=SAF, start_is_M_initially=start_is_M_initially)

				if boundary < tto:
					# it has a marked area:
					if boundary != tfrom and start_is_M_initially:
					# if boundary != tfrom and start_is_M_initially:
						susceptible_intervals += [ (s, [tfrom, boundary]) ]
						direction = 0
					else:
						susceptible_intervals += [ (s, [boundary, tto]) ]
				
				assert (tto - boundary >= 0)
				assert (boundary - tfrom >= 0)


				if direction:
					pos += tto - boundary
					neg += boundary - tfrom

					print("normal")
					current_pos = tto - boundary
					current_neg = boundary - tfrom

				else:
					## region goes backwards
					pos += boundary - tfrom
					neg += tto - boundary
					direction = 1

					print("backwards")
					current_pos = boundary - tfrom
					current_neg = tto - boundary

				# pos += tto - boundary
				# neg += boundary - tfrom				

				pos_per_sig[s] += current_pos

				assert (pos_per_sig[s] <= 1)

				# print(f"From {tfrom} to {tto}")
				# print(f"Boundary = {boundary}")
				# print(f"New susceptible = {current_pos}")
				# print(f"pos = {pos}")
				# print(f"New non-susceptible = {current_neg}")
				# print(f"neg = {neg}")
				# print(f"pos_per_sig[{s}] = {pos_per_sig[s]}")
				# print("--------------------------------------------------")
	
	else:
		victims = tqdm(non_output_signals, leave=True, desc="Victim Signals Progress")
		for s in victims:
			victims.write("--------------------------------------------------")
			victims.write(f"SIGNAL {count} = {s}")
			victims.write("--------------------------------------------------")
			count+=1
			for i in range(len(times)-1):
				tfrom = times[i]
				tto = times[i+1]
				start_is_M_initially = isSusceptibleSA(t=tfrom, s=s, states=states, events=events, T=T, output_signals=output_signals, SAF=SAF, MafterGrid=ERROR)
				boundary = findBoundarySA(tfrom=tfrom, tto=tto, s=s, states=states, events=events, T=T, output_signals=output_signals, SAF=SAF, start_is_M_initially=start_is_M_initially)

				if boundary < tto:
					# it has a marked area:
					if boundary != tfrom and start_is_M_initially:
					# if boundary != tfrom and start_is_M_initially:
						susceptible_intervals += [ (s, [tfrom, boundary]) ]
						direction = 0
					else:
						susceptible_intervals += [ (s, [boundary, tto]) ]
				
				assert (tto - boundary >= 0)
				assert (boundary - tfrom >= 0)

				if direction:
					pos += tto - boundary
					neg += boundary - tfrom

					print("normal")
					current_pos = tto - boundary
					current_neg = boundary - tfrom

				else:
					## region goes backwards
					pos += boundary - tfrom
					neg += tto - boundary
					direction = 1

					print("backwards")
					current_pos = boundary - tfrom
					current_neg = tto - boundary

				# pos += tto - boundary
				# neg += boundary - tfrom				

				pos_per_sig[s] += current_pos

				assert (pos_per_sig[s] <= 1)

				# print(f"From {tfrom} to {tto}")
				# print(f"Boundary = {boundary}")
				# print(f"New susceptible = {current_pos}")
				# print(f"pos = {pos}")
				# print(f"New non-susceptible = {current_neg}")
				# print(f"neg = {neg}")
				# print(f"pos_per_sig[{s}] = {pos_per_sig[s]}")
				# print("--------------------------------------------------")
						

			# 	print(f"before {pos_per_sig[s]}")
			# 	pos_per_sig[s] += pos
			# 	print(f"after {pos_per_sig[s]}")
			# print("------------POS UPDATED FOR SIGNAL",s,pos_per_sig[s],"------------")		
		
	for s in output_signals:
		pos_per_sig[s] += times[-1] - times[0]

		if not exclude_output_signals:
			susceptible_intervals += [ (s, [times[0], times[-1]]) ]
			pos += times[-1] - times[0]

			# if times[i] <= cutoff_max and times[i+1] >= cutoff_min:
			#     # region overlaps with cropped region
			#     t_from = max(cutoff_min, times[i])
			#     t_to =   min(cutoff_max, times[i+1])

			#     if was_M:
			#         susceptible_intervals += [ (s, [t_from, t_to]) ]
			#         pos += t_to - t_from
			#     else:
			#         neg += t_to - t_from

	p = pos/(pos+neg) if pos + neg > 0 else 'undefined'
	p_per_sig = { s: pos_per_sig[s] / (times[-1] - times[0]) for s in signals }

	assert (p <= 1)
	assert (p_per_sig[s] <= 1 for s in signals)

	return {
		'p': p,
		'p_per_sig': p_per_sig,
		'cutoff_min': cutoff_min,
		'cutoff_max': cutoff_max,
		'susceptible': susceptible_intervals
	}