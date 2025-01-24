from tqdm import tqdm
from seal import tracem as tr
import logging

logger = logging.getLogger(__name__)
ERROR = 1e-6
error_cause=False
step_count = 0

def isSusceptibleSA(t, s, states, events, T, output_signals, SAF, MafterGrid,	#	MafterGrid=0.001
					snk_delay=10, src_delay=10,
					monitor=False, tokens=None, input_widths=None, output_widths=None): 
		
	events_check = events + [
		(t + MafterGrid, s, SAF),           # add SA0 or SA1
	]
	times_M, states_M = tr.traceSA(states[0], events_check, output_signals, SA_signal=s, SA_value=SAF, SA_time=t+MafterGrid,
								T=T, snk_delay=snk_delay, src_delay=src_delay,
								monitor=monitor, tokens=tokens, input_widths=input_widths, output_widths=output_widths, verbose=False) #	Mdelay=t+MafterGrid,
	
	was_M = False
	for state_M in states_M:
		was_M = was_M or any([ state_M[s] == 0.5 for s in output_signals ])	

	# print((f"SA_signal {s} stuck at {SAF} at time {t+MafterGrid} {was_M}"))
	return was_M
				

def findDelta(s, tfrom, tto, times, inititally_r=True, inititally_d=True):

	# assert tto-tfrom > ERROR, f"[{tfrom}, {tto}]"
	# error_cause=False
	outputList = tr.getOutputList(s)
	delta_candidates = []
	# print(outputList)
	global error_cause
	# error_cause=True
	global step_count

	step_count +=1

	# final output and no feedback
	if not outputList:
		delta = [tfrom, tto]
		return delta
	
	for output in outputList:
		temp_sig = output[0]
		temp_d = output[1]
		temp_tfrom = tfrom + temp_d
		temp_tto = tto + temp_d

		# crosses T
		if temp_tfrom >= times[-1]:
			delta = [tfrom, tto]
			return delta

		if temp_tto > times[-1]:
			temp_tto = times[-1]
			error_cause=True

		for t in times:
			# crosses time boundary/region
			if t > temp_tfrom and t < temp_tto:
				# adjust delta bound
				temp_tto = t
				break

		# test next level
		temp_delta = findDelta(temp_sig, temp_tfrom, temp_tto, times, inititally_r=False, inititally_d=False) #, visited=visited)
		delta_candidates.append([temp_delta[0] - temp_d, temp_delta[1] - temp_d])

		assert len(delta_candidates)==1	
		return min(delta_candidates)


def checkSA(times, states, events, signals, output_signals,
	snk_delay=10, src_delay=10,
	Textra=30,
	exclude_output_signals=True,
	cutoff_min=0, cutoff_max=float('Inf'),
	fault='SA0',
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

	if fault == 'SA0':
		SAF = 0
	elif fault == 'SA1':
		SAF = 1

	non_output_signals = [ s for s in signals if s not in output_signals ]

	if monitor:
		if tokens is None or input_widths is None or output_widths is None:
			raise Exception("Tokens and In/Output Widths missing!")
		
	global step_count

	# go over regions
	count=0
	if victim_signals:
		# to test only a set of signals
		victims = tqdm(victim_signals, leave=True, desc=f"Victim Signals Progress for {fault}")
	else:
		# testing all signals
		victims = tqdm(non_output_signals, leave=True, desc=f"Victim Signals Progress for {fault}")

	for s in victims:
		logger.debug("checking signal %s", s)
		# victims.write("--------------------------------------------------")
		# victims.write(f"SIGNAL {count} = {s}")
		# victims.write("--------------------------------------------------")
		count+=1

		for i in range(len(times)-1):
			tfrom = times[i]
			tto = times[i+1]
			logger.debug("checking time %s", tfrom)

			delta = [tfrom, tfrom]

			while True:
				# step 1: find the smallest delta
				delta = findDelta(s, delta[1], tto, times, inititally_r=False)
				# print(f"delta for signal {s} is {delta}")
				# print("delta type is ", type(delta))
				mid_point = (delta[0] + delta[1]) / 2

				assert (delta[1] - delta[0] > 0), f"{delta[1]}, {delta[0]}, {error_cause}"
				
				# step 2: inject a fault anywhere within delta
				region_is_M = isSusceptibleSA(t=mid_point, s=s, states=states, events=events, T=T, output_signals=output_signals, SAF=SAF, MafterGrid=ERROR,
								snk_delay=snk_delay, src_delay=src_delay,
								monitor=monitor, tokens=tokens, input_widths=input_widths, output_widths=output_widths)
				
				# step 3: label the delta region (and add to pos & neg & pos_per_sig[s] accordingly)
				if region_is_M:
					susceptible_intervals += [ (s, [delta[0], delta[1]]) ]
					pos += delta[1] - delta[0]
					pos_per_sig[s] += delta[1] - delta[0]
				else:
					neg += delta[1] - delta[0]

				if delta[1] >= tto:
					print(f"Steps for signal {s} for time region {tfrom} to {tto} = {step_count}")
					step_count = 0
					break

		
	for s in output_signals:
		pos_per_sig[s] += times[-1] - times[0]

		if not exclude_output_signals:
			susceptible_intervals += [ (s, [times[0], times[-1]]) ]
			pos += times[-1] - times[0]


	p = pos/(pos+neg) if pos + neg > 0 else 'undefined'
	if victim_signals:
		p_per_sig = { s: pos_per_sig[s] / (times[-1] - times[0]) for s in victims }
	else:
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