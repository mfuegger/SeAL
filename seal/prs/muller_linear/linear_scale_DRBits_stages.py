import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + "/../../")

import numpy as np
import math as m
from libs import tracem as tr


def GeneratePipeline(num_stages=3, num_bits=2):
    # circuit (at least 3 stages/2 input bits)
    # 8 dual-rail bits linear pipeline

    a = np.array(num_bits)
    b = np.array(num_bits)

    steps = int(m.log2(num_bits))

    c_dict = {}
    for c in range(steps):
        c_dict[f"list{c+1}"] = []

    # Start circuit

    for i in range(1, num_stages + 1):
        # Last stage (ackin)
        if i == num_stages:
            tr.rise(f=tr.INVr, i=["ackin"], o=f"en{i}", d=2)
            tr.fall(f=tr.INVf, i=["ackin"], o=f"en{i}", d=2)

        else:
            # inv_2                 ack3        en2
            tr.rise(f=tr.INVr, i=[f"ack{i+1}"], o=f"en{i}", d=2)
            tr.fall(f=tr.INVf, i=[f"ack{i+1}"], o=f"en{i}", d=2)

        for j in range(num_bits):
            # First stage (inputs aF, aT, bF & bT)
            if i == 1:
                # c_a1F[0]
                tr.rise(f=tr.Cr, i=[f"aF[{j}]", f"en{i}"], o=f"ca{i}F[{j}]", d=5)
                tr.fall(f=tr.Cf, i=[f"aF[{j}]", f"en{i}"], o=f"ca{i}F[{j}]", d=5)

                # c_a1T[0]
                tr.rise(f=tr.Cr, i=[f"aT[{j}]", f"en{i}"], o=f"ca{i}T[{j}]", d=5)
                tr.fall(f=tr.Cf, i=[f"aT[{j}]", f"en{i}"], o=f"ca{i}T[{j}]", d=5)

                # c_b1F[0]
                tr.rise(f=tr.Cr, i=[f"bF[{j}]", f"en{i}"], o=f"cb{i}F[{j}]", d=5)
                tr.fall(f=tr.Cf, i=[f"bF[{j}]", f"en{i}"], o=f"cb{i}F[{j}]", d=5)

                # c_b1T[0]
                tr.rise(f=tr.Cr, i=[f"bT[{j}]", f"en{i}"], o=f"cb{i}T[{j}]", d=5)
                tr.fall(f=tr.Cf, i=[f"bT[{j}]", f"en{i}"], o=f"cb{i}T[{j}]", d=5)

            # Intermediate stages (input of stage is ouput of previous one)
            else:
                # c_a2F[0]                  ca1F[0]     en2            ca2F[0]
                tr.rise(f=tr.Cr, i=[f"ca{i-1}F[{j}]", f"en{i}"], o=f"ca{i}F[{j}]", d=5)
                tr.fall(f=tr.Cf, i=[f"ca{i-1}F[{j}]", f"en{i}"], o=f"ca{i}F[{j}]", d=5)

                # c_a2T[0]                 ca1T[0]      en2            ca2T[0]
                tr.rise(f=tr.Cr, i=[f"ca{i-1}T[{j}]", f"en{i}"], o=f"ca{i}T[{j}]", d=5)
                tr.fall(f=tr.Cf, i=[f"ca{i-1}T[{j}]", f"en{i}"], o=f"ca{i}T[{j}]", d=5)

                # c_b2F[0]              cb1F[0]         en2             cb2F[0]
                tr.rise(f=tr.Cr, i=[f"cb{i-1}F[{j}]", f"en{i}"], o=f"cb{i}F[{j}]", d=5)
                tr.fall(f=tr.Cf, i=[f"cb{i-1}F[{j}]", f"en{i}"], o=f"cb{i}F[{j}]", d=5)

                # c_b2T[0]              cb1T[0]         en2             cb2T[0]
                tr.rise(f=tr.Cr, i=[f"cb{i}F[{j}]", f"en{i}"], o=f"cb{i}T[{j}]", d=5)
                tr.fall(f=tr.Cf, i=[f"cb{i}F[{j}]", f"en{i}"], o=f"cb{i}T[{j}]", d=5)

            # OR gate per bit for completion detection
            # or_a20                 ca2F[0]         ca2T[0]         ora21
            tr.rise(f=tr.ORr, i=[f"ca{i}F[{j}]", f"ca{i}T[{j}]"], o=f"ora{i}{j}", d=4)
            tr.fall(f=tr.ORf, i=[f"ca{i}F[{j}]", f"ca{i}T[{j}]"], o=f"ora{i}{j}", d=4)

            # or_b20                 cb2F[0]         cb2T[0]         orb20
            tr.rise(f=tr.ORr, i=[f"cb{i}F[{j}]", f"cb{i}T[{j}]"], o=f"orb{i}{j}", d=4)
            tr.fall(f=tr.ORf, i=[f"cb{i}F[{j}]", f"cb{i}T[{j}]"], o=f"orb{i}{j}", d=4)

            # MCE to check when both inputs belong to the same context
            # c_or21            ora20           orb20           cor20
            tr.rise(f=tr.Cr, i=[f"ora{i}{j}", f"orb{i}{j}"], o=f"cor{i}{j}", d=5)
            tr.fall(f=tr.Cf, i=[f"ora{i}{j}", f"orb{i}{j}"], o=f"cor{i}{j}", d=5)

            c_dict["list1"].append(f"cor{i}{j}")

        for c in range(steps):
            # Last MCE to join/merge all other MCEs (last step)
            if c + 1 == steps:
                # DEBUG
                # for c in range(3):
                #     print(c_dict.keys())
                #     print(f'list{steps}')
                #     print(len(c_dict[f'list{c+1}']))
                #     print(c_dict[f'list{steps}'])

                # First Stage (ackout)
                if i == 1:
                    tr.rise(
                        f=tr.Cr,
                        i=[
                            str(c_dict[f"list{steps}"][0]),
                            str(c_dict[f"list{steps}"][1]),
                        ],
                        o="ackout",
                        d=5,
                    )
                    tr.fall(
                        f=tr.Cf,
                        i=[
                            str(c_dict[f"list{steps}"][0]),
                            str(c_dict[f"list{steps}"][1]),
                        ],
                        o="ackout",
                        d=5,
                    )
                # All other stages (ack_i)
                else:
                    # ack2				c_dict[list1[0]]
                    tr.rise(
                        f=tr.Cr,
                        i=[
                            str(c_dict[f"list{steps}"][0]),
                            str(c_dict[f"list{steps}"][1]),
                        ],
                        o=f"ack{i}",
                        d=5,
                    )
                    tr.fall(
                        f=tr.Cf,
                        i=[
                            str(c_dict[f"list{steps}"][0]),
                            str(c_dict[f"list{steps}"][1]),
                        ],
                        o=f"ack{i}",
                        d=5,
                    )
            # Intermediate MCEs (intermediate steps)
            else:
                # which MCE we are creating
                # iterate over the elements of the list in 2s
                for index in range(0, len(c_dict[f"list{c+1}"]), 2):
                    tr.rise(
                        f=tr.Cr,
                        i=[
                            str(c_dict[f"list{c+1}"][index]),
                            str(c_dict[f"list{c+1}"][index + 1]),
                        ],
                        o=f"{'c'*(c+2)}{i}{index}",
                        d=5,
                    )
                    tr.fall(
                        f=tr.Cf,
                        i=[
                            str(c_dict[f"list{c+1}"][index]),
                            str(c_dict[f"list{c+1}"][index + 1]),
                        ],
                        o=f"{'c'*(c+2)}{i}{index}",
                        d=5,
                    )

                    c_dict[f"list{c+2}"].append(f"{'c'*(c+2)}{i}{index}")

                    # for cc in range(num_bits/pow(2, c+1)):
                    # # c_ackout        cor10           cor11           cc1
                    # tr.rise(f=tr.Cr, i=[f'cor1{c}', f'cor1{c+1}'], o=f'cc{c+1}', d=5)
                    # tr.fall(f=tr.Cf, i=[f'cor1{c}', f'cor1{c+1}'], o=f'cc{c+1}', d=5)

        # Clear lists for new stage
        for c in range(steps):
            c_dict[f"list{c+1}"].clear()

    #######################################################
    # pprint.pprint(rules)
    # pprint.pprint(signals)

    # run it

    init = {
        "aF[0]": 1,
        "aT[0]": 0,
        "bF[0]": 1,
        "bT[0]": 0,
        "aF[1]": 0,
        "aT[1]": 1,
        "bF[1]": 0,
        "bT[1]": 1,
        "en1": 0,
        "ca1F[0]": 1,
        "ca1T[0]": 0,
        "ora10": 1,
        "ca1F[1]": 0,
        "ca1T[1]": 1,
        "ora11": 1,
        "cor10": 1,
        "cb1F[0]": 1,
        "cb1T[0]": 0,
        "orb10": 1,
        "cb1F[1]": 0,
        "cb1T[1]": 1,
        "orb11": 1,
        "cor11": 1,
        "ackout": 1,
        "en2": 0,
        "ca2F[0]": 1,
        "ca2T[0]": 0,
        "ora20": 1,
        "ca2F[1]": 0,
        "ca2T[1]": 1,
        "ora21": 1,
        "cor20": 1,
        "cb2F[0]": 1,
        "cb2T[0]": 0,
        "orb20": 1,
        "cb2F[1]": 0,
        "cb2T[1]": 1,
        "orb21": 1,
        "cor21": 1,
        "ack2": 1,
        "en3": 0,
        "ca3F[0]": 1,
        "ca3T[0]": 0,
        "ora30": 1,
        "ca3F[1]": 0,
        "ca3T[1]": 1,
        "ora31": 1,
        "cor30": 1,
        "cb3F[0]": 1,
        "cb3T[0]": 0,
        "orb30": 1,
        "cb3F[1]": 0,
        "cb3T[1]": 1,
        "orb31": 1,
        "cor31": 1,
        "ack3": 1,
        "ackin": 1,
        # Uncomment for 8 input bits
        # 'aF[2]': 1,
        # 'aT[2]': 0,
        # 'bF[2]': 1,
        # 'bT[2]': 0,
        # 'aF[3]': 0,
        # 'aT[3]': 1,
        # 'bF[3]': 0,
        # 'bT[3]': 1,
        # 'ca1F[2]': 1,
        # 'ca1T[2]': 0,
        # 'ora12': 1,
        # 'cb1F[2]': 1,
        # 'cb1T[2]': 0,
        # 'orb12': 1,
        # 'cor12': 1,
        # 'ca1F[3]': 0,
        # 'ca1T[3]': 1,
        # 'ora13': 1,
        # 'cb1F[3]': 0,
        # 'cb1T[3]': 1,
        # 'orb13': 1,
        # 'cor13': 1,
        # 'cc10': 1,
        # 'cc12': 1,
        # 'ca2F[2]': 1,
        # 'ca2T[2]': 0,
        # 'ora22': 1,
        # 'cb2F[2]': 1,
        # 'cb2T[2]': 0,
        # 'orb22': 1,
        # 'cor22': 1,
        # 'ca2F[3]': 0,
        # 'ca2T[3]': 1,
        # 'ora23': 1,
        # 'cb2F[3]': 0,
        # 'cb2T[3]': 1,
        # 'orb23': 1,
        # 'cor23': 1,
        # 'cc20': 1,
        # 'cc22': 1,
        # 'ca3F[2]': 1,
        # 'ca3T[2]': 0,
        # 'ora32': 1,
        # 'cb3F[2]': 1,
        # 'cb3T[2]': 0,
        # 'orb32': 1,
        # 'cor32': 1,
        # 'ca3F[3]': 0,
        # 'ca3T[3]': 1,
        # 'ora33': 1,
        # 'cb3F[3]': 0,
        # 'cb3T[3]': 1,
        # 'orb33': 1,
        # 'cor33': 1,
        # 'cc30': 1,
        # 'cc32': 1,
    }

    events = [
        (5, "aF[0]", 0),
        (5, "aT[1]", 0),
        (10, "bF[0]", 0),
        (10, "bT[1]", 0),
        (44, "ackin", 0),
        (50, "aT[0]", 1),
        (50, "aF[1]", 1),
        (55, "bT[0]", 1),
        (55, "bF[1]", 1),
        (84, "ackin", 1),
        (60, "aT[0]", 0),
        (60, "aF[1]", 0),
        (65, "bT[0]", 0),
        (65, "bF[1]", 0),
        (100, "ackin", 0),
        (110, "aF[0]", 1),
        (110, "aT[1]", 1),
        (120, "bF[0]", 1),
        (120, "bT[1]", 1),
        (150, "ackin", 1),
        # Uncomment for 8 input bits
        # (5, 'aF[2]', 0),
        # (5, 'aT[3]', 0),
        # (10, 'bF[2]', 0),
        # (10, 'bT[3]', 0),
        # (50, 'aT[2]', 1),
        # (50, 'aF[3]', 1),
        # (55, 'bT[2]', 1),
        # (55, 'bF[3]', 1),
        # (60, 'aT[2]', 0),
        # (60, 'aF[3]', 0),
        # (65, 'bT[2]', 0),
        # (65, 'bF[3]', 0),
        # (110, 'aF[2]', 1),
        # (110, 'aT[3]', 1),
        # (120, 'bF[2]', 1),
        # (120, 'bT[3]', 1),
    ]

    output_signals = [
        "ca3F[0]",
        "ca3T[0]",
        "ca3F[1]",
        "ca3T[1]",
        "cb3F[0]",
        "cb3T[0]",
        "cb3F[1]",
        "cb3T[1]",
        # Uncomment for 8 input bits
        #   'ca3F[2]',
        #   'ca3T[2]',
        #   'ca3F[3]',
        #   'ca3T[3]',
        #   'cb3F[2]',
        #   'cb3T[2]',
        #   'cb3F[3]',
        #   'cb3T[3]',
        "ackout",
    ]

    return init, events, output_signals
