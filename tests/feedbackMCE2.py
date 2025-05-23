from docopt import docopt
import time
import pprint
from seal import tracem as tr
from seal import plotting
from seal import preprocessing as p


usage_msg = """

TODO
Explain what the script does
cutoff


usage:
    feedbackMCE2.py [options]

Options:
-h --help                   Show this screen.
-v --version                Show version information.

--runtime=T                 Time for execution prefix.
                            [default: 50].       
--fault=F                   Fault type to check (possible values: SA0, SA1, SAF)
                            [default: SAF].            
--testcase                  Check a specific fault injection.
--delta2                    Check using checkdelta2.
--deltaopt                  Check using checkdeltaopt.
--nomasking                 Disable the improved masking algorithm.        
--plotaffectedpoints        Plot the affected points.        
"""
# --------|---------|---------|---------|---------|---------|---------|---------|


def main():
    options = docopt(usage_msg, version="0.1")

    # --------|---------|---------|---------|---------|
    if options["--delta2"]:
        from seal import checkdelta2 as check
    elif options["--deltaopt"]:
        from seal import checkdeltaopt as check
    else:
        from seal import checkdelta as check
    # --------|---------|---------|---------|---------|

    T = float(options["--runtime"])
    fault = str(options["--fault"])
    assert fault in ["SAF", "SA1", "SA0"], "Fault type not supported"

    if options["--testcase"]:
        CHECK = False
    else:
        CHECK = True

    # circuit
    delays = {
        "buf_b": 2,
        "inv_b1": 3,
        "MCE_out": 0.5,
    }

    # buf1
    tr.rise(f=tr.BUFr, i=["b1"], o="b", d=delays["buf_b"])
    tr.fall(f=tr.BUFf, i=["b1"], o="b", d=delays["buf_b"])

    # MCE3
    tr.rise(f=tr.Cr, i=["a", "b"], o="out", d=delays["MCE_out"])
    tr.fall(f=tr.Cf, i=["a", "b"], o="out", d=delays["MCE_out"])

    # inv1
    tr.rise(f=tr.INVr, i=["out"], o="b1", d=delays["inv_b1"])
    tr.fall(f=tr.INVf, i=["out"], o="b1", d=delays["inv_b1"])

    init = {"a": 0, "b1": 0, "b": 0, "out": 0}

    events = [
        (7, "a", 1),
        (19, "a", 0),
        (27, "a", 1),
        (39, "a", 0),
    ]

    output_signals = ["out"]

    if not CHECK:
        print("running testcase")
        stuck_sig = "b1"
        stuck_value = 1
        stuck_t = 30.6

        events += [
            (stuck_t, stuck_sig, stuck_value),
        ]
        times, states = tr.traceSA(
            init, events, output_signals, stuck_sig, stuck_value, stuck_t, T=T
        )

    else:
        times, states = tr.trace(init, events, output_signals, T=T)

    plotting.plot(
        times,
        states,
        list(init.keys()),
        init,
        events,
        delays=None,
        fname="feedbackMCE2.svg",
    )

    # # print it
    # for i in range(len(times)):
    #     print()
    #     print(f"time {times[i]}:")
    #     pprint.pprint(states[i])

    # cutoff
    cutoff_min = 0
    cutoff_max = float("Inf")

    if CHECK:
        start = time.time()

        SA1_M = {}
        SA0_M = {}

        if fault == "SAF" or fault == "SA1":
            SA1_M = check.checkSA(
                times=times,
                states=states,
                events=events,
                signals=list(init.keys()),
                output_signals=output_signals,
                cutoff_min=cutoff_min,
                cutoff_max=cutoff_max,
                fault="SA1",
                plot_affected_points=options["--plotaffectedpoints"],
                use_masking=not options["--nomasking"],
                # victim_signals=[]
            )
            pprint.pprint(SA1_M)

        if fault == "SAF" or fault == "SA0":
            SA0_M = check.checkSA(
                times=times,
                states=states,
                events=events,
                signals=list(init.keys()),
                output_signals=output_signals,
                cutoff_min=cutoff_min,
                cutoff_max=cutoff_max,
                fault="SA0",
                # victim_signals=[]
                plot_affected_points=options["--plotaffectedpoints"],
                use_masking=not options["--nomasking"],
            )
            pprint.pprint(SA0_M)

        end = time.time()

        susceptible_SA1 = p.appendSAF(
            p.collapseRanges(SA1_M["susceptible"] if SA1_M else []), "SA1"
        )
        susceptible_SA0 = p.appendSAF(
            p.collapseRanges(SA0_M["susceptible"] if SA0_M else []), "SA0"
        )
        susceptible = susceptible_SA1 + susceptible_SA0

        total_time = end - start
        print(f"\n time to check circuit using checkdelta is {total_time}")

        plotting.plot(
            times,
            states,
            list(init.keys()),
            init,
            events,
            delays=None,
            susceptible=susceptible,
            fault=fault,
            cutoff=[cutoff_min, cutoff_max],
            fname="feedbackMCE2.svg",
        )


if __name__ == "__main__":
    main()
