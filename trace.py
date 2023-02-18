import pprint
import copy

Cr = lambda a,b: min(a,b)
Cf = lambda a,b: min(1-a,1-b)

INVr = lambda a: 1-a
INVf = lambda a: a

rules = []
signals = []

def getSignals():
	global signals
	return signals


def rule(f, i, o, val, d=1):
	global rules, signals
	rules += [ {'f': f, 'i': i, 'o': o, 'val': val, 'd': d} ]
	for s in i + [ o ]:
		if s not in signals:
			signals += [ s ]
			

def eval_rule(state, rule):
	args = [ state[s] for s in rule['i'] ]
	return rule['f'](*args)


def rise(f, i, o, d=1):
	"""
	add a rising PR
	"""
	rule(f=f, i=i, o=o, val=1, d=d)


def fall(f, i, o, d=1):
	"""
	add a falling PR
	"""
	rule(f=f, i=i, o=o, val=0, d=d)


def trace(init, events=[], T=20, Mdelay=0.1):
	"""
	init:   initial state. Dict of the form: signal -> value
	events: list of items (time, signal, value)
	T:      time until execution
	"""
	global rules, signals
	t = 0
	states = []
	times = []

	# check if something is initialized that is not in the circuit
	for s in init.keys():
		if s not in signals:
			print(f'warning: initalized signal {s} does not appear in the circuit. Ignoring it.')
	
	# init
	state = dict()
	for s in signals:
		state[s] = init[s] if s in init.keys() else 0
		if s not in init.keys():
			print(f'warning: did not find initial state for signal {s}. Assuming 0.')

	# follow up
	scheduled = []
	while t <= T:
		# check events: keep only if still true
		# print()
		# print(state)
		# print('scheduled at time', t, scheduled)

		# --- apply unstable rule effects ---

		# unstable events:
		#   list of the rules that were scheduled, but that now evaluate not to 1 (they are 0 or 0.5)
		unstable_rules = [ event[1] for event in scheduled if eval_rule(state=state, rule=event[1]) < 1 ]

		# for all these: make glitch at output immediately if the current value and the intended value do not match
		for rule in unstable_rules:
			# print('unstable at time', t, rule)
			new_value = rule['val'] if ( state[ rule['o'] ] == rule['val'] ) else 0.5
			state[ rule['o'] ] = new_value
			assert (new_value == 0.5)


		# --- apply stable & scheduled rule effects ---

		# keep only stable events in scheduled
		scheduled = [ event for event in scheduled if eval_rule(state=state, rule=event[1]) == 1 ]

		# apply events:
		#   find the ones that are scheduled for time t
		#   apply these
		rules_to_apply = [ event[1] for event in scheduled if event[0] == t ]
		for rule in rules_to_apply:
			# print('apply at time', t, rule)
			state[ rule['o'] ] = rule['val']


		# --- apply external events ---

		# potentially overwrite with external events
		for event in events:
			if event[0] == t:
				state[ event[1] ] = event[2]
		

		# --- update state ---

		# add state
		times  += [ t ]
		states += [ copy.deepcopy(state) ]

		# keep only future events
		scheduled = [ event for event in scheduled if event[0] > t ]
		events =    [ event for event in events    if event[0] > t ]

		# --- schedule new events ---

		# schedule new events
		for rule in rules:
			# if rule guard is true and effect not already the case in state
			if eval_rule(state, rule) > 0:
				if eval_rule(state, rule) == 1 and state[ rule['o'] ] != rule['val']:
					scheduled += [ (t + rule['d'], rule) ]

				elif eval_rule(state, rule) == 0.5 and state[ rule['o'] ] != 0.5:
					# print('propagate M')
					new_rule = copy.deepcopy(rule)
					new_rule['val'] = 0.5
					scheduled += [ (t + Mdelay, new_rule) ]
				
		# next time from:
		#  T,
		#  scheduled event,
		#  external event
		if t < T:
			next_t = min([ T ] + [ event[0] for event in scheduled ] + [ event[0] for event in events ])
			t = next_t

		else:
			# reached T
			break

	# filter (if no change in state -> remove it)
	# this could be done more efficiently in the first place
	state = None
	filtered_times = []
	filtered_states = []
	for i in range(len(states)):
		if i == len(states)-1:
			# last state -> always add
			filtered_times += [ times[i] ]
			filtered_states += [ states[i] ]

		else:
			# before last state -> filter if did not change
			if str(state) != str(states[i]):
				filtered_times += [ times[i] ]
				filtered_states += [ states[i] ]
				state = states[i]

	return filtered_times, filtered_states

