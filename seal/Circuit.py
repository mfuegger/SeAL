from collections import namedtuple

class Circuit:
    State = dict[str, float]
    Event = tuple[float, str, float]
    # EventT = namedtuple('EventT', ['time', 'signal', 'value'])
    Trace = tuple[list[float], list[State]]
    # TraceT = namedtuple('TraceT', ['times', 'states'])

    rules = []
    signals: list[str] = []
    init = dict[str, float]
    events = list[Event]
    # ------------------
    tokens = []
    input_widths = []
    # ------------------
    output_signals = []
    # ------------------
    output_widths = []

    def __init__(self, name):
        self.name = name

    def ToCode(self) -> str:
        output = f"{self.name}.T = {self.T}, {self.name}.F = {self.F}"
        # attributes = (" " + self.Attributes.ToCode()).rstrip()
        return output  # + attributes + ";"

    def __str__(self):
        out = f'Circuit {self.name}\n'
        out += f'Rules {len(self.rules)}\n'
        out += f'Signals {len(self.signals)}\n'
        out += f'Events {len(self.events)}\n'
        out += f'Tokens {self.tokens}\n'
        out += f'Input Widths {self.input_widths}\n'
        out += f'Output Signals {self.output_signals}\n'
        out += f'Output Widths {self.output_widths}\n'
        return out
    
    def __repr__(self):
        return self.ToCode()
    
    def getSignals(self) -> list[str]:
        return self.signals


    def getDelays(self) -> list[float]:
        """
        get delays of all PRs as sorted list
        """
        ret = sorted(list(set([rule["d"] for rule in self.rules])))
        return ret


    def getInflunceList(self, o: str):
        """
        for PRs of the form

        G1 -> o = b [d]

        it returns [ (a, d), (b, d), ... ]
        where a, b, ... are the variables in G
        """
        ret = [(sig, rule["d"]) for rule in self.rules for sig in rule["i"] if rule["o"] == o]
        return ret


    def getInflunceTimeList(self, o: str) -> list[float]:
        """
        for PRs of the form

        G1 -> o = b [d1]
        G1 -> o = b [d2]

        it returns [ d1, d2 ]
        """
        ret = [rule["d"] for rule in self.rules if rule["o"] == o]
        return ret


    def getOutputList(self, i: str) -> list[str, float]:
        # remove duplicates because of rising/falling -> set
        ret = list(set([(rule["o"], rule["d"]) for rule in self.rules if i in rule["i"]]))
        return ret


    def getOutputListAll(self):
        outputListDict = dict()
        for sig in self.signals:
            outputListDict[sig] = self.getOutputList(sig)
        return outputListDict

# --------------------------------------------------
    def clear(self) -> None:
        """
        clears the circuit
        """
        self.rules = []
        self.signals = []
# --------------------------------------------------

    def rule(self, f, i, o, val, d: float = 1):
        self.rules += [{"f": f, "i": i, "o": o, "val": val, "d": d}]
        for s in i + [o]:
            if s not in self.signals:
                self.signals += [s]


    # def eval_rule(state, rule):
    #     args = [state[s] for s in rule["i"]]
    #     # x = rule['f'](*args)
    #     return rule["f"](*args)


    def rise(self, f, i, o, d: float = 1):
        """
        add a rising PR
        """
        self.rule(f=f, i=i, o=o, val=1, d=d)


    def fall(self, f, i, o, d: float = 1):
        """
        add a falling PR
        """
        self.rule(f=f, i=i, o=o, val=0, d=d)
