from seal import tracem as tr


def GeneratePipeline():
    # circuit
    # Muller Pipeline (linear)
    # 1-dual-rail-bit 3-stage linear pipeline
    # with half-adder logic between first 2 buffer stages

    tr.rise(
        f=tr.Cr,
        i=["half_adder__a(0).F", "half_adder__b(0).F"],
        o="half_adder__aFbF",
        d=5,
    )
    tr.fall(
        f=tr.Cf,
        i=["half_adder__a(0).F", "half_adder__b(0).F"],
        o="half_adder__aFbF",
        d=5,
    )

    tr.rise(
        f=tr.Cr,
        i=["half_adder__a(0).F", "half_adder__b(0).T"],
        o="half_adder__aFbT",
        d=5,
    )
    tr.fall(
        f=tr.Cf,
        i=["half_adder__a(0).F", "half_adder__b(0).T"],
        o="half_adder__aFbT",
        d=5,
    )

    tr.rise(
        f=tr.Cr,
        i=["half_adder__a(0).T", "half_adder__b(0).F"],
        o="half_adder__aTbF",
        d=5,
    )
    tr.fall(
        f=tr.Cf,
        i=["half_adder__a(0).T", "half_adder__b(0).F"],
        o="half_adder__aTbF",
        d=5,
    )

    tr.rise(
        f=tr.Cr,
        i=["half_adder__a(0).T", "half_adder__b(0).T"],
        o="r2__sum_in(1).T",
        d=5,
    )
    tr.fall(
        f=tr.Cf,
        i=["half_adder__a(0).T", "half_adder__b(0).T"],
        o="r2__sum_in(1).T",
        d=5,
    )

    tr.rise(
        f=tr.ORr, i=["half_adder__aFbF", "r2__sum_in(1).T"], o="r2__sum_in(0).F", d=6
    )
    tr.fall(
        f=tr.ORf, i=["half_adder__aFbF", "r2__sum_in(1).T"], o="r2__sum_in(0).F", d=6
    )

    tr.rise(
        f=tr.ORr, i=["half_adder__aTbF", "half_adder__aFbT"], o="r2__sum_in(0).T", d=6
    )
    tr.fall(
        f=tr.ORf, i=["half_adder__aTbF", "half_adder__aFbT"], o="r2__sum_in(0).T", d=6
    )

    tr.rise(
        f=tr.ORr,
        i=["half_adder__a(0).F", "half_adder__b(0).F"],
        o="r2__sum_in(1).F",
        d=6,
    )
    tr.fall(
        f=tr.ORf,
        i=["half_adder__a(0).F", "half_adder__b(0).F"],
        o="r2__sum_in(1).F",
        d=6,
    )

    tr.rise(f=tr.INVr, i=["r1__en_n"], o="r1__en", d=2)
    tr.fall(f=tr.INVf, i=["r1__en_n"], o="r1__en", d=2)

    tr.rise(f=tr.INVr, i=["r1__in_done"], o="r1__in_done_n", d=2)
    tr.fall(f=tr.INVf, i=["r1__in_done"], o="r1__in_done_n", d=2)

    tr.rise(f=tr.Cr, i=["r3__in_done", "r1__in_done_n"], o="r1__en_n", d=5)
    tr.fall(f=tr.Cf, i=["r3__in_done", "r1__in_done_n"], o="r1__en_n", d=5)

    tr.rise(f=tr.ORr, i=["chin_a(0).F", "chin_a(0).T"], o="r1__ic_0", d=6)
    tr.fall(f=tr.ORf, i=["chin_a(0).F", "chin_a(0).T"], o="r1__ic_0", d=6)

    tr.rise(f=tr.Cr, i=["chin_a(0).F", "r1__en"], o="half_adder__a(0).F", d=5)
    tr.fall(f=tr.Cf, i=["chin_a(0).F", "r1__en"], o="half_adder__a(0).F", d=5)

    tr.rise(f=tr.Cr, i=["r1__en", "chin_a(0).T"], o="half_adder__a(0).T", d=5)
    tr.fall(f=tr.Cf, i=["r1__en", "chin_a(0).T"], o="half_adder__a(0).T", d=5)

    tr.rise(f=tr.ORr, i=["half_adder__a(0).T", "half_adder__a(0).F"], o="r1__c_0", d=6)
    tr.fall(f=tr.ORf, i=["half_adder__a(0).T", "half_adder__a(0).F"], o="r1__c_0", d=6)

    tr.rise(f=tr.ORr, i=["chin_b(0).F", "chin_b(0).T"], o="r1__ic_1", d=6)
    tr.fall(f=tr.ORf, i=["chin_b(0).F", "chin_b(0).T"], o="r1__ic_1", d=6)

    tr.rise(f=tr.Cr, i=["r1__en", "chin_b(0).F"], o="half_adder__b(0).F", d=5)
    tr.fall(f=tr.Cf, i=["r1__en", "chin_b(0).F"], o="half_adder__b(0).F", d=5)

    tr.rise(f=tr.Cr, i=["r1__en", "chin_b(0).T"], o="half_adder__b(0).T", d=5)
    tr.fall(f=tr.Cf, i=["r1__en", "chin_b(0).T"], o="half_adder__b(0).T", d=5)

    tr.rise(f=tr.ORr, i=["half_adder__b(0).T", "half_adder__b(0).F"], o="r1__c_1", d=6)
    tr.fall(f=tr.ORf, i=["half_adder__b(0).T", "half_adder__b(0).F"], o="r1__c_1", d=6)

    tr.rise(f=tr.Cr, i=["r1__ic_1", "r1__ic_0"], o="r1__in_done", d=5)
    tr.fall(f=tr.Cf, i=["r1__ic_1", "r1__ic_0"], o="r1__in_done", d=5)

    tr.rise(f=tr.Cr, i=["r1__c_1", "r1__c_0"], o="chin_ack", d=5)
    tr.fall(f=tr.Cf, i=["r1__c_1", "r1__c_0"], o="chin_ack", d=5)

    tr.rise(f=tr.INVr, i=["r2__en_n"], o="r2__en", d=2)
    tr.fall(f=tr.INVf, i=["r2__en_n"], o="r2__en", d=2)

    tr.rise(f=tr.INVr, i=["r2__in_done"], o="r2__in_done_n", d=2)
    tr.fall(f=tr.INVf, i=["r2__in_done"], o="r2__in_done_n", d=2)

    tr.rise(f=tr.Cr, i=["r2__ack_in", "r2__in_done_n"], o="r2__en_n", d=5)
    tr.fall(f=tr.Cf, i=["r2__ack_in", "r2__in_done_n"], o="r2__en_n", d=5)

    tr.rise(f=tr.ORr, i=["r2__sum_in(0).F", "r2__sum_in(0).T"], o="r2__ic_0", d=6)
    tr.fall(f=tr.ORf, i=["r2__sum_in(0).F", "r2__sum_in(0).T"], o="r2__ic_0", d=6)

    tr.rise(f=tr.Cr, i=["r2__sum_in(0).F", "r2__en"], o="r3__sum_in(0).F", d=5)
    tr.fall(f=tr.Cf, i=["r2__sum_in(0).F", "r2__en"], o="r3__sum_in(0).F", d=5)

    tr.rise(f=tr.Cr, i=["r2__sum_in(0).T", "r2__en"], o="r3__sum_in(0).T", d=5)
    tr.fall(f=tr.Cf, i=["r2__sum_in(0).T", "r2__en"], o="r3__sum_in(0).T", d=5)

    tr.rise(f=tr.ORr, i=["r3__sum_in(0).T", "r3__sum_in(0).F"], o="r3__ic_0", d=6)
    tr.fall(f=tr.ORf, i=["r3__sum_in(0).T", "r3__sum_in(0).F"], o="r3__ic_0", d=6)

    tr.rise(f=tr.ORr, i=["r2__sum_in(1).F", "r2__sum_in(1).T"], o="r2__ic_1", d=6)
    tr.fall(f=tr.ORf, i=["r2__sum_in(1).F", "r2__sum_in(1).T"], o="r2__ic_1", d=6)

    tr.rise(f=tr.Cr, i=["r2__sum_in(1).F", "r2__en"], o="r3__sum_in(1).F", d=5)
    tr.fall(f=tr.Cf, i=["r2__sum_in(1).F", "r2__en"], o="r3__sum_in(1).F", d=5)

    tr.rise(f=tr.Cr, i=["r2__en", "r2__sum_in(1).T"], o="r3__sum_in(1).T", d=5)
    tr.fall(f=tr.Cf, i=["r2__en", "r2__sum_in(1).T"], o="r3__sum_in(1).T", d=5)

    tr.rise(f=tr.ORr, i=["r3__sum_in(1).F", "r3__sum_in(1).T"], o="r3__ic_1", d=6)
    tr.fall(f=tr.ORf, i=["r3__sum_in(1).F", "r3__sum_in(1).T"], o="r3__ic_1", d=6)

    tr.rise(f=tr.Cr, i=["r2__ic_1", "r2__ic_0"], o="r2__in_done", d=5)
    tr.fall(f=tr.Cf, i=["r2__ic_1", "r2__ic_0"], o="r2__in_done", d=5)

    tr.rise(f=tr.Cr, i=["r3__ic_1", "r3__ic_0"], o="r3__in_done", d=5)
    tr.fall(f=tr.Cf, i=["r3__ic_1", "r3__ic_0"], o="r3__in_done", d=5)

    tr.rise(f=tr.INVr, i=["r3__en_n"], o="r3__en", d=2)
    tr.fall(f=tr.INVf, i=["r3__en_n"], o="r3__en", d=2)

    tr.rise(f=tr.INVr, i=["r3__in_done"], o="r3__in_done_n", d=2)
    tr.fall(f=tr.INVf, i=["r3__in_done"], o="r3__in_done_n", d=2)

    tr.rise(f=tr.Cr, i=["chout_ack", "r3__in_done_n"], o="r3__en_n", d=5)
    tr.fall(f=tr.Cf, i=["chout_ack", "r3__in_done_n"], o="r3__en_n", d=5)

    tr.rise(f=tr.Cr, i=["r3__en", "r3__sum_in(0).F"], o="chout_sum(0).F", d=5)
    tr.fall(f=tr.Cf, i=["r3__en", "r3__sum_in(0).F"], o="chout_sum(0).F", d=5)

    tr.rise(f=tr.Cr, i=["r3__en", "r3__sum_in(0).T"], o="chout_sum(0).T", d=5)
    tr.fall(f=tr.Cf, i=["r3__en", "r3__sum_in(0).T"], o="chout_sum(0).T", d=5)

    tr.rise(f=tr.ORr, i=["chout_sum(0).F", "chout_sum(0).T"], o="r3__c_0", d=6)
    tr.fall(f=tr.ORf, i=["chout_sum(0).F", "chout_sum(0).T"], o="r3__c_0", d=6)

    tr.rise(f=tr.Cr, i=["r3__en", "r3__sum_in(1).F"], o="chout_sum(1).F", d=5)
    tr.fall(f=tr.Cf, i=["r3__en", "r3__sum_in(1).F"], o="chout_sum(1).F", d=5)

    tr.rise(f=tr.Cr, i=["r3__en", "r3__sum_in(1).T"], o="chout_sum(1).T", d=5)
    tr.fall(f=tr.Cf, i=["r3__en", "r3__sum_in(1).T"], o="chout_sum(1).T", d=5)

    tr.rise(f=tr.ORr, i=["chout_sum(1).F", "chout_sum(1).T"], o="r3__c_1", d=6)
    tr.fall(f=tr.ORf, i=["chout_sum(1).F", "chout_sum(1).T"], o="r3__c_1", d=6)

    tr.rise(f=tr.Cr, i=["r3__c_0", "r3__c_1"], o="r2__ack_in", d=5)
    tr.fall(f=tr.Cf, i=["r3__c_0", "r3__c_1"], o="r2__ack_in", d=5)

    init = {
        "chin_a(0).F": 0,
        "chin_a(0).T": 1,
        "chin_b(0).F": 0,
        "chin_b(0).T": 1,
        "half_adder__aFbF": 0,
        "half_adder__aFbT": 0,
        "half_adder__aTbF": 0,
        "r2__sum_in(1).T": 0,
        "r2__sum_in(0).F": 0,
        "r2__sum_in(0).T": 0,
        "r2__sum_in(1).F": 0,
        "r1__en": 0,
        "r1__in_done_n": 0,
        "r1__en_n": 0,
        "r1__ic_0": 0,
        "half_adder__a(0).F": 0,
        "half_adder__a(0).T": 0,
        "r1__c_0": 0,
        "r1__ic_1": 0,
        "half_adder__b(0).F": 0,
        "half_adder__b(0).T": 0,
        "r1__c_1": 0,
        "r1__in_done": 0,
        "chin_ack": 0,
        "r2__en": 0,
        "r2__in_done_n": 0,
        "r2__en_n": 0,
        "r2__ic_0": 0,
        "r3__sum_in(0).F": 0,
        "r3__sum_in(0).T": 0,
        "r3__ic_0": 0,
        "r2__ic_1": 0,
        "r3__sum_in(1).F": 0,
        "r3__sum_in(1).T": 0,
        "r3__ic_1": 0,
        "r2__in_done": 0,
        "r3__in_done": 0,
        "r3__en": 0,
        "r3__in_done_n": 0,
        "r3__en_n": 0,
        "chout_sum(0).F": 0,
        "chout_sum(0).T": 0,
        "r3__c_0": 0,
        "chout_sum(1).F": 0,
        "chout_sum(1).T": 0,
        "r3__c_1": 0,
        "r2__ack_in": 0,
        "chout_ack": 0,
    }

    events = []

    output_signals = [
        "chin_ack",
        "chout_sum(0).F",
        "chout_sum(0).T",
        "chout_sum(1).F",
        "chout_sum(1).T",
    ]

    return init, events, output_signals
