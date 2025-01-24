from typing import Any
from tqdm import tqdm
from seal import tracem as tr
import logging

ERROR = 1e-6
logger = logging.getLogger(__name__)


def isSusceptibleSA(
    t,
    s,
    states,
    events,
    T,
    output_signals,
    SAF,
    MafterGrid: float,
    snk_delay: float = 10,
    src_delay: float = 10,
    monitor: bool = False,
    tokens=None,
    input_widths=None,
    output_widths=None,
) -> bool:
    # print("isSusceptibleSA", s, t, SAF)
    # add the error event
    events_check = events + [
        (t + MafterGrid, s, SAF),
    ]
    # simulate
    times_M, states_M = tr.traceSA(
        states[0],
        events_check,
        output_signals,
        SA_signal=s,
        SA_value=SAF,
        SA_time=t + MafterGrid,
        T=T,
        snk_delay=snk_delay,
        src_delay=src_delay,
        monitor=monitor,
        tokens=tokens,
        input_widths=input_widths,
        output_widths=output_widths,
        verbose=False,
    )
    # check if was M
    was_M = False
    for state_M in states_M:
        was_M = was_M or any([state_M[s] == 0.5 for s in output_signals])

    return was_M


def findDelta(signal: str, time: float, times: list[float], simulation: tuple, simulation_SA: tuple, history: list[str]=[]) -> float:
    """
    Returns by how much we can proceed.
    """
    # logger.debug("%s:%s", signal, time)
    times_larger = [t for t in times if t > time]
    if len(times_larger) == 0:
        # no more region boundaries ahead -> can proceed as much as wanted
        return float("inf")

    # next region boundary
    end_of_region = min(times_larger)

    # how long to next region boundary
    duration_on_own_signal = end_of_region - time
    ret = [duration_on_own_signal]

    # check if this event would be masked,
    # i.e., simulation(signal, time) == simulation_SA(signal, time)
    # If so, return
    if False:
        return ret[0]

    # Else (i.e., not masked),
    # check recursively on downstream gates
    outputList = tr.getOutputList(signal)
    for output in outputList:
        out_sig = output[0]
        delay = output[1]
        delta = findDelta(out_sig, time + delay, times, simulation=simulation, simulation_SA=simulation_SA, history=history+[f"{signal}:{time}"])
        assert delta > 0
        ret += [delta]

    # combine as minimum
    assert min(ret) > 0
    return min(ret)


def checkSA(
    times: list[float],
    states,
    events,
    signals: list[str],
    output_signals,
    snk_delay: float = 10.0,
    src_delay: float = 10.0,
    Textra: float = 30.0,
    exclude_output_signals=True,
    cutoff_min=0,
    cutoff_max=float("Inf"),
    fault: str = "SA0",
    monitor: bool = False,
    tokens=None,
    input_widths=None,
    output_widths=None,
    victim_signals: list[str] = [],
) -> dict[str, Any]:
    """
    checking all equivalence regions
    """
    susceptible_intervals = []
    pos: float = 0.0
    neg: float = 0.0
    pos_per_sig: dict[str, float] = {s: 0.0 for s in signals}
    T = times[-1] + Textra

    if fault == "SA0":
        SAF = 0
    elif fault == "SA1":
        SAF = 1
    else:
        raise NotImplementedError()

    non_output_signals = [s for s in signals if s not in output_signals]

    if monitor:
        if tokens is None or input_widths is None or output_widths is None:
            raise Exception("Tokens and In/Output Widths missing!")

    # go over regions
    if victim_signals:
        # to test only a set of signals
        victims = tqdm(
            victim_signals, leave=True, desc=f"Victim Signals Progress for {fault}"
        )
    else:
        # testing all signals
        victims = tqdm(
            non_output_signals, leave=True, desc=f"Victim Signals Progress for {fault}"
        )

    # create the simulation without SA fault
    simulation = tr.trace(
        states[0],
        [],
        output_signals,
        T=T,
        snk_delay=snk_delay,
        src_delay=src_delay,
        monitor=monitor,
        tokens=tokens,
        input_widths=input_widths,
        output_widths=output_widths,
        verbose=False,
    )

    for s in victims:
        logger.debug("checking signal %s", s)
        tfrom = times[0]
        while tfrom < times[-1]:
            logger.debug("checking time %s", tfrom)

            # step 0: create simulation with SA
            simulation_SA = tr.traceSA(
                states[0],
                [],
                output_signals,
                SA_signal=s,
                SA_value=SAF,
                SA_time=tfrom + ERROR,
                T=T,
                snk_delay=snk_delay,
                src_delay=src_delay,
                monitor=monitor,
                tokens=tokens,
                input_widths=input_widths,
                output_widths=output_widths,
                verbose=False,
            )

            # step 1: find the smallest delta
            delta = findDelta(s, tfrom, times, simulation=simulation, simulation_SA=simulation_SA)
            mid_point = tfrom + delta / 2

            # step 2: inject a fault anywhere within delta
            region_is_M = isSusceptibleSA(
                t=mid_point,
                s=s,
                states=states,
                events=events,
                T=T,
                output_signals=output_signals,
                SAF=SAF,
                MafterGrid=ERROR,
                snk_delay=snk_delay,
                src_delay=src_delay,
                monitor=monitor,
                tokens=tokens,
                input_widths=input_widths,
                output_widths=output_widths,
            )

            # step 3: label the delta region (and add to pos & neg & pos_per_sig[s] accordingly)
            if region_is_M:
                susceptible_intervals += [(s, [tfrom, tfrom + delta])]
                pos += delta
                pos_per_sig[s] += delta
            else:
                neg += delta

            # step 4: proceed to next time
            tfrom += delta

    for s in output_signals:
        # assume: all is positive
        pos_per_sig[s] += times[-1] - times[0]

        if not exclude_output_signals:
            susceptible_intervals += [(s, [times[0], times[-1]])]
            pos += times[-1] - times[0]

    p = pos / (pos + neg) if pos + neg > 0 else "undefined"
    if victim_signals:
        p_per_sig = {s: pos_per_sig[s] / (times[-1] - times[0]) for s in victims}
    else:
        p_per_sig = {s: pos_per_sig[s] / (times[-1] - times[0]) for s in signals}

    # assert (p <= 1)
    # assert (p_per_sig[s] <= 1 for s in signals)

    return {
        "p": p,
        "p_per_sig": p_per_sig,
        "cutoff_min": cutoff_min,
        "cutoff_max": cutoff_max,
        "susceptible": susceptible_intervals,
    }
