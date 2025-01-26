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
    bufMCE2.py [options]

Options:
-h --help                   Show this screen.
-v --version                Show version information.

--runtime=T                 Time for execution prefix.
                            [default: 100].       
--fault=F                   Fault type to check (possible values: SA0, SA1, SAF)
                            [default: SAF].            
--testcase=0                Check a specific fault injection case.
                            [default: 0].
--delta2                    Check using checkdelta2.
--deltaopt                  Check using checkdeltaopt.
--plotsamplingpoints        Plot the sampling points.     
"""
# --------|---------|---------|---------|---------|---------|---------|---------|


def main() -> None:
    options = docopt(usage_msg, version="0.1")

    # --------|---------|---------|---------|---------|
    if options["--delta2"]:
        from seal import checkdelta2 as check
    elif options["--deltaopt"]:
        from seal import checkdeltaopt as check
    else:
        from seal import checkdelta as check
    # --------|---------|---------|---------|---------|

    T = int(options["--runtime"])
    fault = str(options["--fault"])
    assert fault in ["SAF", "SA1", "SA0"], "Fault type not supported"

    testcase = None
    if options["--testcase"]:
        CHECK = False
        testcase = int(options["--testcase"])
    else:
        CHECK = True

    # circuit
    delays = {"b": 10, "MCE_out": 0.5}

    # buf1
    tr.rise(f=tr.BUFr, i=["b1"], o="b", d=delays["b"])
    tr.fall(f=tr.BUFf, i=["b1"], o="b", d=delays["b"])

    # MCE
    tr.rise(f=tr.Cr, i=["a", "b"], o="out", d=delays["MCE_out"])
    tr.fall(f=tr.Cf, i=["a", "b"], o="out", d=delays["MCE_out"])

    init: tr.State = {"a": 0, "b1": 0, "b": 0, "out": 0}

    events: list[tr.Event] = [
        (10, "a", 1),
        (11, "a", 0),
        (12, "a", 1),
        (13, "a", 0),
        (14, "a", 1),
        (15, "a", 0),
        (16, "a", 1),
        (17, "a", 0),
        (18, "a", 1),
        (19, "a", 0),
        (20, "a", 1),
        (21, "a", 0),
    ]

    output_signals = ["out"]

    if not CHECK:
        if testcase == 0:
            stuck_sig = "b1"
            stuck_value = 1
            stuck_t = 0.5
            events += [
                (stuck_t, stuck_sig, stuck_value),
            ]
            times, states = tr.traceSA(
                init, events, output_signals, stuck_sig, stuck_value, stuck_t, T=T
            )
        elif testcase == 1:
            stuck_sig = "b1"
            stuck_value = 1
            stuck_t = 1.0
            events += [
                (stuck_t, stuck_sig, stuck_value),
            ]
            times, states = tr.traceSA(
                init, events, output_signals, stuck_sig, stuck_value, stuck_t, T=T
            )
        else:
            times, states = tr.trace(init, events, output_signals, T=T)

    else:
        times, states = tr.trace(init, events, output_signals, T=T)

    plotting.plot(
        times, states, list(init.keys()), init, events, delays=None, fname="buf_MCE2.svg"
    )

    # print it
    # for i in range(len(times)):
    #     print()
    #     print(f'time {times[i]}:')
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
                # victim_signals=['b1'],
                victim_signals=[],
                plot_sampling_points=options["--plotsamplingpoints"],
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
                # victim_signals=['b1']
                victim_signals=[],
                plot_sampling_points=options["--plotsamplingpoints"],
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
            delays=None,  # do not add info in svg
            susceptible=susceptible,
            fault=fault,
            cutoff=[cutoff_min, cutoff_max],
            fname="buf_MCE2.svg",
        )


if __name__ == "__main__":
    main()
