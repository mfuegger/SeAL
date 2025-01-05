import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../../')

import pprint
# from libs import tracem as tr
# from libs import plotting
# from libs import checkbi as check
# import math as m

# CHECK = True 	# show sensitivity windows
# CHECK = False	# show effect of specific glitches

# fault = 'SET'
# fault = 'SA0'
# fault = 'SA1'



# create

# ----------------------------------------------------------------------------------------------------------
# init

# ----------------------------------------------------------------------------------------------------------

# run 

# DR_tokens = [
# 	{'op': [op(0).T = 1, op(0).F = 0, op(1).T = 1, op(1).F = 0], 'a': [a(0).T = 1, a(0).F = 0, a(1).T = 1, a(1).F = 0, a(2).T = 0, a(2).F = 1, a(3).T = 0, a(3).F = 1], 'b': [b(0).T = 0, b(0).F = 1, b(1).T = 0, b(1).F = 1, b(2).T = 0, b(2).F = 1, b(3).T = 1, b(3).F = 0]},
# 	{'op': [op(0).T = 1, op(0).F = 0, op(1).T = 1, op(1).F = 0], 'a': [a(0).T = 1, a(0).F = 0, a(1).T = 1, a(1).F = 0, a(2).T = 0, a(2).F = 1, a(3).T = 0, a(3).F = 1], 'b': [b(0).T = 0, b(0).F = 1, b(1).T = 0, b(1).F = 1, b(2).T = 0, b(2).F = 1, b(3).T = 1, b(3).F = 0]},
# 	{'op': [op(0).T = 1, op(0).F = 0, op(1).T = 1, op(1).F = 0], 'a': [a(0).T = 1, a(0).F = 0, a(1).T = 1, a(1).F = 0, a(2).T = 0, a(2).F = 1, a(3).T = 0, a(3).F = 1], 'b': [b(0).T = 0, b(0).F = 1, b(1).T = 0, b(1).F = 1, b(2).T = 0, b(2).F = 1, b(3).T = 1, b(3).F = 0]},
# 	{'op': [op(0).T = 1, op(0).F = 0, op(1).T = 1, op(1).F = 0], 'a': [a(0).T = 1, a(0).F = 0, a(1).T = 1, a(1).F = 0, a(2).T = 0, a(2).F = 1, a(3).T = 0, a(3).F = 1], 'b': [b(0).T = 0, b(0).F = 1, b(1).T = 0, b(1).F = 1, b(2).T = 0, b(2).F = 1, b(3).T = 1, b(3).F = 0]},
# 	{'op': [op(0).T = 1, op(0).F = 0, op(1).T = 1, op(1).F = 0], 'a': [a(0).T = 1, a(0).F = 0, a(1).T = 1, a(1).F = 0, a(2).T = 0, a(2).F = 1, a(3).T = 0, a(3).F = 1], 'b': [b(0).T = 0, b(0).F = 1, b(1).T = 0, b(1).F = 1, b(2).T = 0, b(2).F = 1, b(3).T = 1, b(3).F = 0]},
# 	{'op': [op(0).T = 1, op(0).F = 0, op(1).T = 1, op(1).F = 0], 'a': [a(0).T = 1, a(0).F = 0, a(1).T = 1, a(1).F = 0, a(2).T = 0, a(2).F = 1, a(3).T = 0, a(3).F = 1], 'b': [b(0).T = 0, b(0).F = 1, b(1).T = 0, b(1).F = 1, b(2).T = 0, b(2).F = 1, b(3).T = 1, b(3).F = 0]},
# 	{'op': [op(0).T = 1, op(0).F = 0, op(1).T = 1, op(1).F = 0], 'a': [a(0).T = 1, a(0).F = 0, a(1).T = 1, a(1).F = 0, a(2).T = 0, a(2).F = 1, a(3).T = 0, a(3).F = 1], 'b': [b(0).T = 0, b(0).F = 1, b(1).T = 0, b(1).F = 1, b(2).T = 0, b(2).F = 1, b(3).T = 1, b(3).F = 0]},
# 	{'op': [op(0).T = 1, op(0).F = 0, op(1).T = 1, op(1).F = 0], 'a': [a(0).T = 1, a(0).F = 0, a(1).T = 1, a(1).F = 0, a(2).T = 0, a(2).F = 1, a(3).T = 0, a(3).F = 1], 'b': [b(0).T = 0, b(0).F = 1, b(1).T = 0, b(1).F = 1, b(2).T = 0, b(2).F = 1, b(3).T = 1, b(3).F = 0]}
# 	]

#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
class DualRail:
	def __init__(self, name, T=0, F=0):
		self.name = name
		self.T = T
		self.F = F

	def ToCode(self) -> str:
		output = f"{self.name}.T = {self.T}, {self.name}.F = {self.F}"
		# output = f"{self.name}.T = {int(self.T)}, {self.name}.F = {int(self.F)}"
		# attributes = (" " + self.Attributes.ToCode()).rstrip()
		return output #+ attributes + ";"

	# def __str__(self):
	# 	return f'DualRail(T={self.T}, F={self.F})'
	
	
	def __repr__(self):
		return self.ToCode()
	

def toDualRail(input_tokens, input_bits):

	'''
	DR_tokens is a list of dual-rail-input tokens
	each token is a dict of dual-rail inputs
	each dual-rail input has a list of its bits
	each dual-rail bit has true and false values (op(0).T and op(0).F)
	ex: [
		{'op': [op(0).DualRail(T=0, F=1), op(1).DualRail(T=1, F=0)],
		'a': [a(0).DualRail(T=1, F=0), a(1).DualRail(T=1, F=0), a(2).DualRail(T=0, F=1), a(3).DualRail(T=1, F=0)],
		'b': [b(0).DualRail(T=1, F=0), b(1).DualRail(T=1, F=0), b(2).DualRail(T=0, F=1), b(3).DualRail(T=0, F=1)]},
		{...},
		{...},
		]
	'''
	DR_tokens = []
	for token in input_tokens:
		DR_token = {}
		for signal, value in token.items():
			print(50*"-")
			print(f"{signal} = {value}")
			#  each element is of type DualRail
			DR_input = []
			# print("current signal", signal)
			num_bits = input_bits[signal]
			# print("num_bits = ", num_bits)
			bin_str = bin(value)[2:].zfill(num_bits)
			print("binary = ", bin_str)
			# print("----------------------")

			for i, bit in enumerate(bin_str[::-1]):
				# print("binary = ", bin_str)
				# print("current bit index", i)
				# print("current bit = ", bit)
				var_name = f'{signal}({i})'
				print(f"{var_name} = {bit}")
				print(type(bit))
				# print("----------------------")

				x = DualRail(var_name, T=0 if int(bit) == 0 else 1, F=1 if int(bit) == 0 else 0)
				# print(globals()[var_name])
				
				# create variable with dynamic name
				# if var_name not in globals():					
				# 	globals()[var_name] = DualRail(var_name, T=0 if int(bit) == 0 else 1, F=1 if int(bit) == 0 else 0)
				# 	print(globals()[var_name])
				# 	print("----------------------")
				# else:
				# 	print("heeere",globals()[var_name])
				# 	raise Exception(f"Variable {var_name} already exists")
				
				# DR_input.append(globals()[var_name])
				DR_input.append(x)
				print(f"Input bit-width = {len(DR_input)}")
					
			# print(f"{var_name} = {bit}")
			# print(f"{var_name}.T = {globals()[var_name].T} and {var_name}.F = {globals()[var_name].F}")

			DR_token[signal] = DR_input
			print(f"Token Size = {len(DR_token)}")

		DR_tokens.append(DR_token)
		print(f"Tokens length = {len(DR_tokens)}")

	# print(DR_tokens)
	# print(f"Dual-rail token list size = {len(DR_tokens)}")

	# printing
	# for token in DR_tokens: 
	# 	for signal, value in token.items(): # dict (str, list)
	# 		for i, v in enumerate(value):	# list (int, DualRail)
	# 			# print(f"{signal} : {i}")
	# 			# print(f"{signal}({i}).T = {v.T} and {signal}({i}).F = {v.F}")
	# 			print(v.ToCode())

	return DR_tokens
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------

snk_delay = 10
src_delay = 10

events = [(1, 'c1', 0)]

input_widths = {'op': 2, 'a': 4, 'b': 4}

tokens = [{'op': 2, 'a': 1, 'b': 3}, {'op': 2, 'a': 3, 'b': 11}, {'op': 0, 'a': 7, 'b': 12}, {'op': 1, 'a': 8, 'b': 2}, {'op': 1, 'a': 15, 'b': 1}, {'op': 0, 'a': 9, 'b': 4}, {'op': 2, 'a': 9, 'b': 10}, {'op': 3, 'a': 10, 'b': 5}]

output_signals = {'z(3).F', 'z(2).F', 'z(1).F', 'ack_out', 'z(1).T', 'z(3).T', 'z(0).T', 'z(0).F', 'z(2).T'}

output_widths = {'z': 4}

DR_tokens = toDualRail(tokens, input_widths)
DR_tokens_copy = DR_tokens

# list of inputs (add it to prs? then no need to have it here)
# list of data inputs (add it to prs? then no need to have it here)
inputs = []
for key in input_widths:
	inputs.append(key)
# print("inputs:")
# print(inputs)

# list of data outputs
# outputs = output_signals
# outputs.discard('ack_out')
outputs = []
for key in output_widths:
	outputs.append(key)

signal_bits_dict = {}
# Iterate over the input widths dictionary
for signal in output_widths:
	# Initialize an empty set to store single bits for the current input signal
	signal_bits = set()
	
	# Iterate over the output signals set to find single bits corresponding to the current input signal
	for output in output_signals:
		if output.startswith(f"{signal}("):
			# Extract the bit index from the output signal
			bit_index = output.split('(')[1].split(')')[0]
			
			# Add the single bit to the set
			signal_bits.add(f"{signal}({bit_index})")
	
	# Add the set of single bits to the dictionary with the input signal as the key
	signal_bits_dict[signal] = signal_bits
	# print(signal_bits_dict)


'''
	DR_output is a dictionary that contains signal name and a list
	of dual-rail bits initialized to 0
	ex: {'z': [
			[z(1).T = 0, z(1).F = 0],	# DualRail
			[z(0).T = 0, z(0).F = 0],	# DualRail
			[z(3).T = 0, z(3).F = 0],	# DualRail
			[z(2).T = 0, z(2).F = 0]	# DualRail
			],
		'out2' : [...],
		'out3' : [...]
		}
'''
DR_output = {}
for signal, bits in signal_bits_dict.items():	# dict (str, set)
	DR_bit = []

	for bit in bits:	# set (str)
		DR_bit.append(DualRail(bit))
	
	DR_output[signal] = DR_bit

# for signal, value in DR_output.items(): # str, list
	# for i, v in enumerate(value):	# DualRail
		# print(f"{signal} : {i}")
		# print(f"{signal}({i}).T = {v.T} and {signal}({i}).F = {v.F}")
		# print(v.ToCode())
	
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
# testing Dual Rail

DR_tokens = toDualRail(tokens, input_widths)
print("tokens:", tokens)
print("dr_tokens", DR_tokens)

# val = 0
# val_DR = DualRail('val', T=1 if val == 1 else 0, F=1 if val == 0 else 0)
# print(f"val = {val}")
# print(f"val_DR : {val_DR}")

#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
# testing monitorACK
# monitor ack_out to send new data
def monitorACK(ack_out, t):

	input_events=[]

	# copy and remove next token in the list
	current_token = DR_tokens_copy.pop(0)

	'''
	current_token is a dict of dual-rail inputs
	each dual-rail input has a list of its bits
	each dual-rail bit has true and false values (op(0).T and op(0).F)
	ex: {'op': [op(0).DualRail(T=0, F=1), op(1).DualRail(T=1, F=0)],
		'a': [a(0).DualRail(T=1, F=0), a(1).DualRail(T=1, F=0), a(2).DualRail(T=0, F=1), a(3).DualRail(T=1, F=0)],
		'b': [b(0).DualRail(T=1, F=0), b(1).DualRail(T=1, F=0), b(2).DualRail(T=0, F=1), b(3).DualRail(T=0, F=1)]}
	'''
	
	# spacer received, schedule next data token
	if not ack_out:
		for signal, token in current_token.items():	# dict
			for i, v in enumerate(token):	# list (int, DualRail)
				input_events += [(t+src_delay, f"{signal}({i}).T", int(v.T))]
				input_events += [(t+src_delay, f"{signal}({i}).F", int(v.F))]
			# for DR_input in DR_token:	# list
			#     for DR_bit in DR_input:	# DualRail
			#         events += (t+src_delay, f"{DR_bit}.T", v.T)
			#         events += (t+src_delay, f"{DR_bit}.F", v.F)

	# data token received, schedule spacer
	else:
		for signal, token in current_token.items():	# dict
			for i, v in enumerate(token):	# list (int, DualRail)
				input_events += [(t+src_delay, f"{signal}({i}).T", 0)]
				input_events += [(t+src_delay, f"{signal}({i}).F", 0)]

	return input_events

# new_events = monitorACK(1, 5)
# print("events:")
# print(events)
# print("new events:")
# print(new_events)
# events.extend(new_events)
# print("events with new events:")
# print(events)

#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
# testing monitorDATA
# monitor data_out to send new ack
def monitorDATA(data_done, t):
	# add this to events as {t+snkDelay, acki_in, 0}
	if data_done == 1:
		ack_event = (t+snk_delay, 'ack_in', 1)
	else:
		ack_event = (t+snk_delay, 'ack_in', 0)

	return ack_event

def CD(DR_output, ack_in):
	done_bits = []

	for bits in DR_output.values():
		for bit in bits:
			done_bits.append(bit.T | bit.F)

	if ack_in == 0:
		done = done_bits[0]
		for bit in done_bits[1:]:
			done &= bit
		if done:
			return 1
		else:
			return 0

		# if done == 1:
		# 	return True
	else:
		done = not done_bits[0]
		# print(f"done_temp = {done}")
		for bit in done_bits[1:]:
			done &= not bit
			# print(f"done_temp = {done}")
		if done:
			return 0
		else:
			return 1
		
events = []	
ack_in = 1
# z_out = [DualRail('z(0)', T='0', F='1'),
# 		 DualRail('z(1)', T='0', F='1'),
# 		 DualRail('z(2)', T='0', F='1'),
# 		 DualRail('z(3)', T='0', F='0')
# 		 ]

DR_output = {'z': [DualRail('z(0)', T=0, F=0),
		 			DualRail('z(1)', T=0, F=0),
		 			DualRail('z(2)', T=0, F=0),
		 			DualRail('z(3)', T=0, F=0)
		 			]}

# for signal, value in DR_output.items(): # str, list
# 	for i, v in enumerate(value):	# DualRail
# 		print(v.ToCode())
# print(f"events before = {events}")

data_done = CD(DR_output, ack_in)
# print(f"data_done = {data_done} and ack_in = {ack_in}")
if data_done != ack_in:
	ack_event = monitorDATA(data_done, 5)
	events.extend(ack_event)
# print(f"events after = {events}")


