import pprint
from seal import tracem as tr
from seal import plotting
from seal import checkbi as check

# CHECK = False
CHECK = True
# fault_check = 'SET'
fault_check = "SA0"
# fault_check = 'SA1'

# circuit

# MCE1
tr.rise(f=tr.Cr, i=["a1", "a2"], o="a3", d=4)
tr.fall(f=tr.Cf, i=["a1", "a2"], o="a3", d=4)

# MCE2
tr.rise(f=tr.Cr, i=["a3", "a1"], o="a4", d=8)
tr.fall(f=tr.Cf, i=["a3", "a1"], o="a4", d=8)

# MCE3
tr.rise(f=tr.Cr, i=["a3", "a2"], o="a5", d=16)
tr.fall(f=tr.Cf, i=["a3", "a2"], o="a5", d=16)
# tr.rise(f=tr.Cr, i=['a4','a2'], o='a5', d=6)
# tr.fall(f=tr.Cf, i=['a4','a2'], o='a5', d=6)

# inv1
tr.rise(f=tr.INVr, i=["a4"], o="a1", d=1)
tr.fall(f=tr.INVf, i=["a4"], o="a1", d=1)

# inv2
tr.rise(f=tr.INVr, i=["a5"], o="a2", d=1)
tr.fall(f=tr.INVf, i=["a5"], o="a2", d=1)


init = {
    "a1": 0,
    "a2": 0,
    "a3": 0,
    "a4": 1,
    "a5": 1,
}

events = []

T = 100

if not CHECK:
    # glitch_t = 34
    # glitch_t = 22
    glitch_t = 40.9

    events = [
        # (glitch_t, 'a1', 0),
        # (glitch_t, 'a1', 1),
        (glitch_t, "a5", 0),
    ]
    # times, states = tr.traceSA(init, events=events, SA_sig='a1', SA_time=glitch_t, T=T)
    # times, states = tr.traceSA(init, events=events, SA_sig='a1', SA_time=glitch_t, T=T)
    times, states = tr.traceSA(init, events=events, SA_sig="a5", SA_time=glitch_t, T=T)

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
        events=events,
        states=states,
        signals=list(init.keys()),
        output_signals=[
            "a4",
            "a5",
        ],  #'a4','a5',
        cutoff_min=cutoff_min,
        cutoff_max=cutoff_max,
        # exclude_output_signals=False,
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
