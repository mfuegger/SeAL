import pprint
import copy

Cr = lambda a,b: min(a,b)
Cf = lambda a,b: min(1-a,1-b)

INVr = lambda a: 1-a
INVf = lambda a: a

rules = []
signals = set()


def rule(f, i, o, val, d=1):
	global rules, signals
	rules += [ {'f': f, 'i': i, 'o': o, 'val': val, 'd': d} ]
	signals.update(i)
	signals.add(o)


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


def trace(init, events=[], T=20):
	"""
	init:   initial state. Dict of the form: signal -> value
	events: list of items (time, signal, value)
	T:      time until execution
	"""
	global rules, signals
	t = 0
	states = []
	times = []
	
	# init
	state = dict()
	for s in signals:
		state[s] = init[s] if s in init.keys() else 0

	# follow up
	scheduled = []
	while t < T:
		# check events: keep only if still true
		# print()
		# print(state)
		# print('scheduled at time', t, scheduled)

		# unstable events
		unstable_rules = [ event[1] for event in scheduled if eval_rule(state=state, rule=event[1]) == 0 ]

		# for all these: make glitch at output if the current value and the intended value do not match
		for rule in unstable_rules:
			# print('unstable at time', t, rule)
			new_value = rule['val'] if ( state[ rule['o'] ] == rule['val'] ) else 0.5
			state[ rule['o'] ] = new_value

		# keep only stable events in scheduled
		scheduled = [ event for event in scheduled if eval_rule(state=state, rule=event[1]) > 0 ]

		# apply events
		rules_to_apply = [ event[1] for event in scheduled if event[0] == t ]
		for rule in rules_to_apply:
			# print('apply at time', t, rule)
			state[ rule['o'] ] = rule['val']

		# potentially overwrite with external events
		for event in events:
			if event[0] == t:
				state[ event[1] ] = event[2]
		
		# add state
		times += [ t ]
		states += [ copy.deepcopy(state) ]

		# keep only future events
		scheduled = [ event for event in scheduled if event[0] > t ]
		events = [ event for event in events if event[0] > t ]

		# schedule new events
		for rule in rules:
			# if rule guard is true and effect not already the case in state
			if eval_rule(state, rule) > 0 and state[ rule['o'] ] != rule['val']:
				if eval_rule(state, rule) == 1:
					scheduled += [ (t + rule['d'], rule) ]
				else:
					assert( eval_rule(state, rule) == 0.5 )
					new_rule = copy.deepcopy(rule)
					new_rule['val'] = 0.5
					scheduled += [ (t + new_rule['d'], new_rule) ]
				
		# next time:
		#  T,
		#  scheduled event,
		#  external event
		next_t = min([ T ] + [ event[0] for event in scheduled ] + [ event[0] for event in events ])
		t = next_t

	# filter (if no change in state -> remove it)
	# this could be done more efficiently in the first place
	state = None
	filtered_times = []
	filtered_states = []
	for i in range(len(states)):
		if str(state) != str(states[i]):
			filtered_times += [ times[i] ]
			filtered_states += [ states[i] ]
			state = states[i]

	return filtered_times, filtered_states

