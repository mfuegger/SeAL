from docopt import docopt
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + "/../")

import time
import pprint
from libs import tracem as tr
from libs import plotting
from libs import preprocessing as p


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
             
"""
# --------|---------|---------|---------|---------|---------|---------|---------|


def main():
    options = docopt(usage_msg, version="0.1")

    # --------|---------|---------|---------|---------|
    if options["--delta2"]:
        from libs import checkdelta2 as check
    else:
        from libs import checkdelta as check
    # --------|---------|---------|---------|---------|

    T = int(options["--runtime"])
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
        stuck_sig = "b"
        stuck_value = 1
        stuck_t = 12.5

        events += [
            (stuck_t, stuck_sig, stuck_value),
        ]
        times, states = tr.traceSA(
            init, events, output_signals, stuck_sig, stuck_value, stuck_t, T=T
        )

    else:
        times, states = tr.trace(init, events, output_signals, T=T)

    plotting.plot(
        times, states, list(init.keys()), init, events, delays, fname="feedbackMCE2.svg"
    )

    # print it
    for i in range(len(times)):
        print()
        print(f"time {times[i]}:")
        pprint.pprint(states[i])

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
            delays,
            susceptible=susceptible,
            fault=fault,
            cutoff=[cutoff_min, cutoff_max],
            fname="feedbackMCE2.svg",
        )


if __name__ == "__main__":
    main()
