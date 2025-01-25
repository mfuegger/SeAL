class DualRail:
    def __init__(self, name, T=0, F=0):
        self.name = name
        self.T = T
        self.F = F

    def ToCode(self) -> str:
        output = f"{self.name}.T = {self.T}, {self.name}.F = {self.F}"
        # attributes = (" " + self.Attributes.ToCode()).rstrip()
        return output  # + attributes + ";"

    # def __str__(self):
    # 	return f'DualRail(T={self.T}, F={self.F})'

    def __repr__(self):
        return self.ToCode()


def toDualRail(input_tokens, input_bits):
    """
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
    """
    DR_tokens = []
    for token in input_tokens:
        DR_token = {}
        for signal, value in token.items():
            #  each element is of type DualRail
            DR_input = []
            # print("current signal", signal)
            num_bits = input_bits[signal]
            # print("num_bits = ", num_bits)
            bin_str = bin(value)[2:].zfill(num_bits)
            # print(bin_str)

            for i, bit in enumerate(bin_str[::-1]):
                # print("binary = ", bin_str)
                # print("current bit index", i)
                # print("current bit = ", bit)
                var_name = f"{signal}({i})"
                # print(f"{var_name} = {bit}")

                DR_input.append(
                    DualRail(
                        var_name,
                        T=0 if int(bit) == 0 else 1,
                        F=1 if int(bit) == 0 else 0,
                    )
                )
                # print(DR_input[-1])
                # print(f"Input bit-width = {len(DR_input)}")

            # print(f"{var_name} = {bit}")
            # print(f"{var_name}.T = {globals()[var_name].T} and {var_name}.F = {globals()[var_name].F}")

            DR_token[signal] = DR_input
            # print(f"Token Size = {len(DR_token)}")

        DR_tokens.append(DR_token)

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
