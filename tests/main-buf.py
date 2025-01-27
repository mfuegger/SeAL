import pprint
from seal import tracem as tr
from seal import plotting

# from libs import checkbi as check
# from depricated import check

# CHECK = False
CHECK = True
# fault_check = 'SET'
fault_check = "SA0"
# fault_check = 'SA1'

# circuit

# buf1
tr.rise(f=tr.BUFr, i=["a"], o="b", d=3)
tr.fall(f=tr.BUFf, i=["a"], o="b", d=3)

# inv1
tr.rise(f=tr.INVr, i=["b"], o="c", d=3)
tr.fall(f=tr.INVf, i=["b"], o="c", d=3)

# buf2
tr.rise(f=tr.BUFr, i=["c"], o="a", d=2)
tr.fall(f=tr.BUFf, i=["c"], o="a", d=2)

init = {
    "a": 0,
    "b": 0,
    "c": 1,
}

events = []

T = 50

if not CHECK:
    glitch_t = 40

    events = [
        (glitch_t, "a", 0),
    ]
    times, states = tr.traceSA(init, events=events, SA_sig="a", SA_time=glitch_t, T=T)

else:
    times, states = tr.trace(init, events=events, T=T)

plotting.plot(times, states, list(init.keys()))

# print it
for i in range(len(times)):
    print()
    print(f"time {times[i]}:")
    pprint.pprint(states[i])

# cutoff
cutoff_min = 0
cutoff_max = float("Inf")

if CHECK:
    ret = check.checkSA(
        times=times,
        states=states,
        events=events,
        signals=list(init.keys()),
        output_signals=["c"],
        cutoff_min=cutoff_min,
        cutoff_max=cutoff_max,
        fault=fault_check,
    )
    pprint.pprint(ret)

    plotting.plot(
        times,
        states,
        list(init.keys()),
        susceptible=ret["susceptible"],
        fault=fault_check,
        cutoff=[cutoff_min, cutoff_max],
    )
