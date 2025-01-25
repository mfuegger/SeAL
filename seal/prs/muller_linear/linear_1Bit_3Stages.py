import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + "/../../")

from libs import tracem as tr


def GeneratePipeline():
    # circuit
    # Muller Pipeline (linear)
    # 1-bit 3-stage linear pipeline

    # inv1 (source)
    tr.rise(f=tr.INVr, i=["c1"], o="c_in", d=4)
    tr.fall(f=tr.INVf, i=["c1"], o="c_in", d=4)

    # inv2
    tr.rise(f=tr.INVr, i=["c2"], o="en1", d=1)
    tr.fall(f=tr.INVf, i=["c2"], o="en1", d=1)

    # c1
    tr.rise(f=tr.Cr, i=["c_in", "en1"], o="c1", d=5)
    tr.fall(f=tr.Cf, i=["c_in", "en1"], o="c1", d=5)

    # inv3
    tr.rise(f=tr.INVr, i=["c3"], o="en2", d=1)
    tr.fall(f=tr.INVf, i=["c3"], o="en2", d=1)

    # c2
    tr.rise(f=tr.Cr, i=["c1", "en2"], o="c2", d=5)
    tr.fall(f=tr.Cf, i=["c1", "en2"], o="c2", d=5)

    # inv4 (sink)
    tr.rise(f=tr.INVr, i=["c3"], o="en3", d=4)
    tr.fall(f=tr.INVf, i=["c3"], o="en3", d=4)

    # c3
    tr.rise(f=tr.Cr, i=["c2", "en3"], o="c3", d=5)
    tr.fall(f=tr.Cf, i=["c2", "en3"], o="c3", d=5)

    # pprint.pprint(rules)
    # pprint.pprint(signals)

    init = {
        "c_in": 0,
        "en1": 1,
        "c1": 0,
        "en2": 1,
        "c2": 0,
        "en3": 1,
        "c3": 0,
    }

    events = []

    output_signals = ["c1"]  # ['c3', 'c1']

    return init, events, output_signals
