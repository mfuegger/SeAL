import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../../')

from libs import tracem as tr    


def GeneratePipeline():
    # circuit
    # 2 dual-rail-bit 3-stage linear pipeline

    # inv1
    tr.rise(f=tr.INVr, i=['ack2'], o='en1', d=2)
    tr.fall(f=tr.INVf, i=['ack2'], o='en1', d=2)

    # c_a1F
    tr.rise(f=tr.Cr, i=['aF','en1'], o='ca1F', d=5)
    tr.fall(f=tr.Cf, i=['aF','en1'], o='ca1F', d=5)

    # c_a1T
    tr.rise(f=tr.Cr, i=['aT','en1'], o='ca1T', d=5)
    tr.fall(f=tr.Cf, i=['aT','en1'], o='ca1T', d=5)

    # or_a1
    tr.rise(f=tr.ORr, i=['ca1F','ca1T'], o='ora1', d=4)
    tr.fall(f=tr.ORf, i=['ca1F','ca1T'], o='ora1', d=4)


    # c_b1F
    tr.rise(f=tr.Cr, i=['bF','en1'], o='cb1F', d=5)
    tr.fall(f=tr.Cf, i=['bF','en1'], o='cb1F', d=5)

    # c_b1T
    tr.rise(f=tr.Cr, i=['bT','en1'], o='cb1T', d=5)
    tr.fall(f=tr.Cf, i=['bT','en1'], o='cb1T', d=5)

    # or_b1
    tr.rise(f=tr.ORr, i=['cb1F','cb1T'], o='orb1', d=4)
    tr.fall(f=tr.ORf, i=['cb1F','cb1T'], o='orb1', d=4)


    # c_ackout
    tr.rise(f=tr.Cr, i=['ora1','orb1'], o='ackout', d=5)
    tr.fall(f=tr.Cf, i=['ora1','orb1'], o='ackout', d=5)

    #######################################################

    # inv_2
    tr.rise(f=tr.INVr, i=['ack3'], o='en2', d=2)
    tr.fall(f=tr.INVf, i=['ack3'], o='en2', d=2)

    # c_a2F
    tr.rise(f=tr.Cr, i=['ca1F','en2'], o='ca2F', d=5)
    tr.fall(f=tr.Cf, i=['ca1F','en2'], o='ca2F', d=5)

    # c_a2T
    tr.rise(f=tr.Cr, i=['ca1T','en2'], o='ca2T', d=5)
    tr.fall(f=tr.Cf, i=['ca1T','en2'], o='ca2T', d=5)

    # or_a2
    tr.rise(f=tr.ORr, i=['ca2F','ca2T'], o='ora2', d=4)
    tr.fall(f=tr.ORf, i=['ca2F','ca2T'], o='ora2', d=4)


    # c_b2F
    tr.rise(f=tr.Cr, i=['cb1F','en2'], o='cb2F', d=5)
    tr.fall(f=tr.Cf, i=['cb1F','en2'], o='cb2F', d=5)

    # c_b2T
    tr.rise(f=tr.Cr, i=['cb1T','en2'], o='cb2T', d=5)
    tr.fall(f=tr.Cf, i=['cb1T','en2'], o='cb2T', d=5)

    # or_b2
    tr.rise(f=tr.ORr, i=['cb2F','cb2T'], o='orb2', d=4)
    tr.fall(f=tr.ORf, i=['cb2F','cb2T'], o='orb2', d=4)


    # c_ack2
    tr.rise(f=tr.Cr, i=['ora2','orb2'], o='ack2', d=5)
    tr.fall(f=tr.Cf, i=['ora2','orb2'], o='ack2', d=5)

    #######################################################

    # inv3
    tr.rise(f=tr.INVr, i=['ackin'], o='en3', d=2)
    tr.fall(f=tr.INVf, i=['ackin'], o='en3', d=2)

    # c_a3F
    tr.rise(f=tr.Cr, i=['ca2F','en3'], o='ca3F', d=5)
    tr.fall(f=tr.Cf, i=['ca2F','en3'], o='ca3F', d=5)

    # c_a3T
    tr.rise(f=tr.Cr, i=['ca2T','en3'], o='ca3T', d=5)
    tr.fall(f=tr.Cf, i=['ca2T','en3'], o='ca3T', d=5)

    # or_a3
    tr.rise(f=tr.ORr, i=['ca3F','ca3T'], o='ora3', d=4)
    tr.fall(f=tr.ORf, i=['ca3F','ca3T'], o='ora3', d=4)


    # c_b3F
    tr.rise(f=tr.Cr, i=['cb2F','en3'], o='cb3F', d=5)
    tr.fall(f=tr.Cf, i=['cb2F','en3'], o='cb3F', d=5)

    # c_b3T
    tr.rise(f=tr.Cr, i=['cb2T','en3'], o='cb3T', d=5)
    tr.fall(f=tr.Cf, i=['cb2T','en3'], o='cb3T', d=5)

    # or_b3
    tr.rise(f=tr.ORr, i=['cb3F','cb3T'], o='orb3', d=4)
    tr.fall(f=tr.ORf, i=['cb3F','cb3T'], o='orb3', d=4)


    # c_ack3
    tr.rise(f=tr.Cr, i=['ora3','orb3'], o='ack3', d=5)
    tr.fall(f=tr.Cf, i=['ora3','orb3'], o='ack3', d=5)

    #######################################################
    # pprint.pprint(rules)
    # pprint.pprint(signals)

    # run it
    init = {
        # 'en1': 0,
        # 'aF': 0,
        # 'ca1F': 0,
        # 'aT': 0,
        # 'ca1T': 1,
        # 'ora1': 0,
        # 'bF': 0,
        # 'cb1F': 1,
        # 'bT': 0,
        # 'cb1T': 0,
        # 'orb1': 0,	
        # 'ackout': 0,

        # 'en2': 0,
        # 'ca2F': 0,
        # 'ca2T': 1,
        # 'ora2': 0,
        # 'cb2F': 1,
        # 'cb2T': 0,
        # 'orb2': 0,
        # 'ack2': 0,
        
        # 'en3': 0,
        # 'ca3F': 1,
        # 'ca3T': 0,
        # 'ora3': 0,
        # 'cb3F': 1,
        # 'cb3T': 0,
        # 'orb3': 0,
        # 'ack3': 0,
        # 'ackin': 0,




        # 'en1': 1,
        # 'aF': 0,
        # 'ca1F': 0,
        # 'aT': 1,
        # 'ca1T': 0,
        # 'ora1': 0,
        # 'bF': 1,
        # 'cb1F': 0,
        # 'bT': 0,
        # 'cb1T': 0,
        # 'orb1': 0,	
        # 'ackout': 0,

        # 'en2': 1,
        # 'ca2F': 0,
        # 'ca2T': 0,
        # 'ora2': 0,
        # 'cb2F': 0,
        # 'cb2T': 0,
        # 'orb2': 0,
        # 'ack2': 0,
        
        # 'en3': 1,
        # 'ca3F': 0,
        # 'ca3T': 0,
        # 'ora3': 0,
        # 'cb3F': 0,
        # 'cb3T': 0,
        # 'orb3': 0,
        # 'ack3': 0,
        # 'ackin': 0,



        
        'en1': 0,
        'aF': 1,
        'ca1F': 1,
        'aT': 0,
        'ca1T': 0,
        'ora1': 1,
        'bF': 1,
        'cb1F': 1,
        'bT': 0,
        'cb1T': 0,
        'orb1': 1,	
        'ackout': 1,

        'en2': 0,
        'ca2F': 1,
        'ca2T': 0,
        'ora2': 1,
        'cb2F': 1,
        'cb2T': 0,
        'orb2': 1,
        'ack2': 1,
        
        'en3': 0,
        'ca3F': 1,
        'ca3T': 0,
        'ora3': 1,
        'cb3F': 1,
        'cb3T': 0,
        'orb3': 1,
        'ack3': 1,
        'ackin': 1,
    }

    events = [
        (5, 'aF', 0),
        (10, 'bF', 0),
        (44, 'ackin', 0),
        (50, 'aT', 1),
        (55, 'bT', 1),

        # (10, 'aF', 0),
        # (15, 'bF', 0),
        # (49, 'ackin', 0),
        # (55, 'aT', 1),
        # (60, 'bT', 1),
    ]

    output_signals = ['ca3F', 'ca3T', 'cb3F', 'cb3T', 'ackout']

    return init, events, output_signals