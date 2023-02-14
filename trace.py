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


def rise(f, i, o, d=1):
	rule(f=f, i=i, o=o, val=1, d=d)


def fall(f, i, o, d=1):
	rule(f=f, i=i, o=o, val=0, d=d)


def eval_rule(state, rule):
	args = [ state[s] for s in rule['i'] ]
	return rule['f'](*args)


def trace(init, T=20):
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
		scheduled = [ event for event in scheduled if eval_rule(state=state, rule=event[1]) > 0 ]

		# apply events
		rules_to_apply = [ event[1] for event in scheduled if event[0] == t ]
		for rule in rules_to_apply:
			# print('apply at time', t, rule)
			state[ rule['o'] ] = rule['val']
		
		# add state
		times += [ t ]
		states += [ copy.deepcopy(state) ]

		# keep only future events
		scheduled = [ event for event in scheduled if event[0] > t ]

		# schedule new events
		for rule in rules:
			# if rule guard is true and effect not already the case in state
			if eval_rule(state, rule) > 0 and state[ rule['o'] ] != rule['val']:
				scheduled += [ (t + rule['d'], rule) ]
				
		# next time
		next_t = min([T] + [ event[0] for event in scheduled ])
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



# ---- testing ------

# circuit

# c
rise(f=Cr, i=['a','b'], o='y', d=2)
fall(f=Cf, i=['a','b'], o='y', d=2)

# inv
rise(f=INVr, i=['y'], o='a', d=4)
fall(f=INVf, i=['y'], o='a', d=4)

# inv
rise(f=INVr, i=['y'], o='b', d=5)
fall(f=INVf, i=['y'], o='b', d=5)

# inv
#rise(f=INVr, i=['y'], o='z', d=1)
#fall(f=INVf, i=['y'], o='z', d=1)

# pprint.pprint(rules)
# pprint.pprint(signals)

# run it
init = {'a': 1, 'b': 1, 'y': 0, 'z': 0}
times, states = trace(init)

# print it
for i in range(len(times)):
	print()
	print(f'time {times[i]}:')
	pprint.pprint(states[i])
