import copy
from collections import namedtuple
from seal import DualRail as DR
from seal.Circuit import Circuit

State = dict[str, float]
Event = tuple[float, str, float]
EventT = namedtuple('EventT', ['time', 'signal', 'value'])
Trace = tuple[list[float], list[State]]
TraceT = namedtuple('TraceT', ['times', 'states'])

def eval_rule(state, rule):
    args = [state[s] for s in rule["i"]]
    # x = rule['f'](*args)
    return rule["f"](*args)

def nr_transitions_in_simulation(states: list[State]) -> int:
    count: int = 0
    old_state = states[0]
    for i in range(1,len(states)):
        new_state = states[i]
        for s in new_state:
            if old_state[s] != new_state[s]:
                count += 1
    return count

def value_at_trace(signal: str, time: float, trace: Trace) -> float:
    """
    Returns the value of the signal at time in the trace.
    """
    times = trace[0]
    states = trace[1]
    assert len(times) == len(states)
    idx = max([i for i in range(len(times)) if times[i] <= time])
    return states[idx][signal]


def trace(
    c: Circuit,    

    # init: dict[str, float],
    # events: list[Event],
    # output_signals: list[str],

    T: float = 50.0,
    snk_delay: float = 10.0,
    src_delay: float = 10.0,
    Mdelay: float = 0.1,    ## which value as default?

    SAF: bool = False,
    SA_signal: str = None,
    SA_value: int = None,
    SA_time: float = None,

    monitor: bool = False,
    # tokens=None,
    # input_widths=None,
    # output_widths=None,
    verbose=True,
) -> tuple[list[float], list[State]]:
    
    """
    init:   initial state. Dict of the form: signal -> value
    events: list of items (time, signal, value)
    T:      time until execution
    tokens: input tokens to feed the circuit
    """
    # global rules, signals
    t: float = 0.0
    states: list[State] = []
    times: list[float] = []

    # check if something is initialized that is not in the circuit
    for s in c.init.keys():
        if s not in c.signals:
            print(
                f"warning: initalized signal {s} does not appear in the circuit. Ignoring it."
            )

    # init
    state: dict[str, float] = dict()
    for s in c.signals:
        state[s] = c.init[s] if s in c.init.keys() else 0
        if s not in c.init.keys():
            print(f"warning: did not find initial state for signal {s}. Assuming 0.")

    """
    visited dict
    keeps track of a signal when it gets scheduled
    as stable for the first time
    to avoid duplicates for the same scheduled value
    and avoid state explosion
    """
    visited_stable: dict[str, bool] = dict()
    for s in c.signals:
        visited_stable[s] = False

    if SAF:
        if SA_signal is None or SA_value is None or SA_time is None:
            raise Exception("Missing stuck-at parameters")

    # --------------------------------------- Monitor Prepocessing ---------------------------------------
    if monitor:
        if c.tokens is None or c.input_widths is None or c.output_widths is None:
            raise Exception("Tokens and In/Output Widths missing!")
        else:
            DR_tokens = DR.toDualRail(c.tokens, c.input_widths)
            DR_tokens_copy = DR_tokens.copy()
            tokens_copy = c.tokens.copy()

            # list of data inputs (add it to prs? then no need to have it here)
            inputs = []
            for key in c.input_widths:
                inputs.append(key)

            # list of data outputs
            # outputs = output_signals
            # outputs.discard('ack_out')
            outputs = []
            for key in c.output_widths:
                outputs.append(key)

            signal_bits_dict = {}
            # Iterate over the input widths dictionary
            for signal in c.output_widths:
                # Initialize an empty set to store single bits for the current input signal
                signal_bits = set()

                # Iterate over the output signals set to find single bits corresponding to the current input signal
                for output in c.output_signals:
                    if output.startswith(f"{signal}("):
                        # Extract the bit index from the output signal
                        bit_index = output.split("(")[1].split(")")[0]

                        # Add the single bit to the set
                        signal_bits.add(f"{signal}({bit_index})")

                # Add the set of single bits to the dictionary with the input signal as the key
                signal_bits_dict[signal] = signal_bits
                # print(signal_bits_dict)

            """
            DR_output is a dictionary that contains signal name and a list
            of dual-rail bits initialized to 0
            ex: {'z': [DualRail('z(0)', T=0, F=0),
                        DualRail('z(1)', T=0, F=0),
                        DualRail('z(2)', T=0, F=0),
                        DualRail('z(3)', T=0, F=0)
                        ],
                'out2' : [...],
                'out3' : [...]
                }
            """
            DR_output = {}
            for signal, bits in signal_bits_dict.items():  # dict (str, set)
                DR_bit = []

                for bit in bits:  # set (str)
                    DR_bit.append(DR.DualRail(bit))

                DR_output[signal] = DR_bit

            # for signal, value in DR_output.items(): # str, list
            #   for i, v in enumerate(value):   # DualRail
            #       print(v.ToCode())

    # ---------------------------------------------------------------------------------------------------

    # ---------------------------------------- Monitor Functions ----------------------------------------
    # monitor ack_out to send new data
    def monitorACK(ack_out, t):
        # list of events in the form (time, signal, value)
        input_events = []

        """
        current_token is a dict of dual-rail inputs
        each dual-rail input has a list of its bits
        each dual-rail bit has true and false values (op(0).T and op(0).F)
        ex: {'op': [op(0).DualRail(T=0, F=1), op(1).DualRail(T=1, F=0)],
            'a': [a(0).DualRail(T=1, F=0), a(1).DualRail(T=1, F=0), a(2).DualRail(T=0, F=1), a(3).DualRail(T=1, F=0)],
            'b': [b(0).DualRail(T=1, F=0), b(1).DualRail(T=1, F=0), b(2).DualRail(T=0, F=1), b(3).DualRail(T=0, F=1)]}
        """

        # spacer received, schedule next data token
        if not ack_out:
            if len(DR_tokens_copy) == 0:
                for signal, token in DR_tokens[0].items():  # dict
                    for i, v in enumerate(token):  # list (int, DualRail)
                        input_events += [(0, f"{signal}({i}).T", 0)]
                        input_events += [(0, f"{signal}({i}).F", 0)]
            else:
                # copy and remove next token in the list
                current_token_notDR = tokens_copy.pop(0)
                current_token = DR_tokens_copy.pop(0)
                next_token = current_token_notDR

                for signal, token in current_token.items():  # dict
                    for i, v in enumerate(token):  # list (int, DualRail)
                        input_events += [(t + src_delay, f"{signal}({i}).T", int(v.T))]
                        input_events += [(t + src_delay, f"{signal}({i}).F", int(v.F))]
                        # input_events += [(t+random.uniform(0.9*src_delay, 1.1*src_delay), f"{signal}({i}).T", int(v.T))]
                        # input_events += [(t+random.uniform(0.9*src_delay, 1.1*src_delay), f"{signal}({i}).F", int(v.F))]

        # data token received, schedule spacer
        else:
            next_token = "SPACER"
            # print("DR_tokens = ", DR_tokens)
            for signal, token in DR_tokens[0].items():  # dict
                for i, v in enumerate(token):  # list (int, DualRail)
                    input_events += [(t + src_delay, f"{signal}({i}).T", 0)]
                    input_events += [(t + src_delay, f"{signal}({i}).F", 0)]
                    # input_events += [(t+random.uniform(0.9*src_delay, 1.1*src_delay), f"{signal}({i}).T", 0)]
                    # input_events += [(t+random.uniform(0.9*src_delay, 1.1*src_delay), f"{signal}({i}).F", 0)]

        return input_events

    # monitor data_out to send new ack
    def monitorDATA(data_done, t):
        # add this to events as {t+snkDelay, acki_in, 0}
        if data_done == 1:
            ack_event = (t + snk_delay, "ack_in", 1)
            # ack_event = (t+random.uniform(0.9*snk_delay, 1.1*snk_delay), 'ack_in', 1)
        else:
            ack_event = (t + snk_delay, "ack_in", 0)
            # ack_event = (t+random.uniform(0.9*snk_delay, 1.1*snk_delay), 'ack_in', 0)

        return ack_event

    def CD(DR_output, ack_in) -> float:
        # if any(DR_output = 0.5):
        #   return ack_in

        for bits in DR_output.values():
            for bit in bits:
                if bit.T == 0.5 or bit.F == 0.5:
                    return ack_in

        done_bits = []

        for bits in DR_output.values():
            for bit in bits:
                done_bits.append(bit.T | bit.F)

        if ack_in == 0:
            # ANDing all the bits
            done = done_bits[0]
            for bit in done_bits[1:]:
                done &= bit
            if done:
                return 1
            else:
                return 0

        else:
            # NORing all the bits
            done = not done_bits[0]
            for bit in done_bits[1:]:
                done &= not bit
            if done:
                return 0
            else:
                return 1

    # ---------------------------------------------------------------------------------------------------

    # follow up
    # schedule first token or spacer
    if monitor:
        input_events = monitorACK(state["ack_out"], t)
        c.events.extend(input_events)    

    scheduled = []
    while t <= T:

        # --- apply external events ---

        # external events
        for event in c.events:
            if event[0] == t:
            # if event.time == t:  
                if not SAF:
                    state[event[1]] = event[2]
                else:
                    if event[1] == SA_signal and event[0] >= SA_time:
                        state[event[1]] = SA_value
                    else:
                        state[event[1]] = event[2]

                    if t >= SA_time:
                        if state[SA_signal] != SA_value:
                            # print("1st events")
                            print(
                                f"SA_signal {SA_signal} became stuck at {SA_value} at time {SA_time} and is not stuck anymore at time {t}!"
                            )


        # --- apply unstable rule effects ---

        # unstable events: (irrespective of time, should always appear after t=Mdelay)
        #   list of the rules that were scheduled, but that now evaluate not to 1 (they are 0 (M gen) or 0.5(M prop))
        unstable_rules = [
            event[1] for event in scheduled if eval_rule(state=state, rule=event[1]) < 1
        ]

        # for all these: make glitch at output immediately if the current value and the intended value do not match
        for rule in unstable_rules:
            # logical mitigation
            new_value = rule["val"] if (state[rule["o"]] == rule["val"]) else 0.5
            if (new_value == 0.5) and (state[rule["o"]] != rule["val"]) and verbose:
                input_parameter_str = ", ".join([f"{s}={state[s]}" for s in rule["i"]])
                print(
                    f"time {t}: M due to unstable rule G({input_parameter_str}) -> {rule['o']} (currently {state[rule['o']]}, setting to {rule['val']})"
                )
            state[rule["o"]] = new_value

            # if SAF:
            #     if t >= SA_time:
            #         if state[SA_signal] != SA_value:
            #             print("unstable_rules")

        # --- apply stable & scheduled rule effects ---

        # keep only stable events in scheduled
        scheduled = [
            event for event in scheduled if eval_rule(state=state, rule=event[1]) == 1
        ]

        # apply events:
        #   find the ones that are scheduled for time t
        #   apply these
        rules_to_apply = [event[1] for event in scheduled if event[0] == t]
        for rule in rules_to_apply:
            temp_state = state[rule["o"]]
            state[rule["o"]] = rule["val"]
            visited_stable[rule["o"]] = False

            # monitor
            if monitor:
                if rule["o"] == "ack_out":
                    # if ack_out made a transition
                    if temp_state != state[rule["o"]]:
                        input_events = monitorACK(state[rule["o"]], t)
                        c.events.extend(input_events)


                elif rule["o"] in c.output_signals:
                    # update the specific rail in DR_output
                    for signal, bits in DR_output.items():  # dict
                        # print(bits)
                        for bit in bits:  # list (DualRail)
                            bit.T = state[f"{bit.name}.T"]
                            bit.F = state[f"{bit.name}.F"]

                    ack_in = state["ack_in"]
                    done = CD(DR_output, ack_in)
                    # if done made a transition
                    if done != ack_in:
                        ack_event = monitorDATA(done, t)
                        c.events.append(ack_event)

            # if SAF:
            #     if t >= SA_time:
            #         if state[SA_signal] != SA_value:
            #             print("rules_to_apply")


        # --- again apply external events if they were overwritten by a state change ---

        # external events
        for event in c.events:
            if event[0] == t:
                if not SAF:
                    state[event[1]] = event[2]
                else:
                    if event[1] == SA_signal and event[0] >= SA_time:
                        state[event[1]] = SA_value
                    else:
                        state[event[1]] = event[2]

                    if t >= SA_time:
                        if state[SA_signal] != SA_value:
                            print("2nd events")
                            print(
                                f"SA_signal {SA_signal} became stuck at {SA_value} at {SA_time} and is not stuck anymore at time {t}!"
                            )


        # --- update state ---

        # add state
        times += [t]
        states += [copy.deepcopy(state)]

        # keep only future events
        scheduled = [event for event in scheduled if event[0] > t]
        c.events = [event for event in c.events if event[0] > t]

        # --- schedule new events ---

        # check if the current state of the circuit affects any of the gates
        # schedule new events
        for rule in c.rules:
            if SAF:
                # if the rule concerns the SA_signal after it got stuck
                # don't schedule a new event and keep the signal stuck
                # regardless of its value to be
                if rule["o"] == SA_signal and t + rule["d"] >= SA_time:
                    continue

            # if rule guard is true and effect not already the case in state
            if (eval_rule(state, rule) > 0) and (state[rule["o"]] != rule["val"]):
                if eval_rule(state, rule) == 1:
                    if not visited_stable[rule["o"]]:
                        scheduled += [(t + rule["d"], rule)]
                        visited_stable[rule["o"]] = True

                # this is only M propagation
                elif eval_rule(state, rule) == 0.5 and (state[rule["o"]] != 0.5):
                    # if not visited_unstable[ rule['o'] ]:
                    new_rule = copy.deepcopy(rule)
                    new_rule["val"] = 0.5
                    scheduled += [(t + Mdelay, new_rule)]
                    # visited_unstable[ rule['o'] ] = True

        if SAF:
            if t > SA_time:
                if state[SA_signal] != SA_value:
                    print(f"SA_signal {SA_signal} = {state[SA_signal]} at time {t}")
                    raise Exception(
                        f"SA_signal {SA_signal} became stuck at {SA_value} at {SA_time} and is not stuck anymore at time {t}!"
                    )

        # next time from:
        #  T,
        #  scheduled event,
        #  external event
        if t < T:
            next_t = min(
                [T] + [event[0] for event in scheduled] + [event[0] for event in c.events]
            )
            t = next_t

        else:
            # reached T
            break

    # filter (if no change in state -> remove it)
    # this could be done more efficiently in the first place
    state = None
    filtered_times: list[float] = []
    filtered_states: list[State] = []
    for i in range(len(states)):
        if i == len(states) - 1:
            # last state -> always add
            filtered_times += [times[i]]
            filtered_states += [states[i]]

        else:
            # before last state -> filter if did not change
            if str(state) != str(states[i]):
                filtered_times += [times[i]]
                filtered_states += [states[i]]
                state = states[i]

    return filtered_times, filtered_states

