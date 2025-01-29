from itertools import count
from typing import Any
from numpy import sign
from tqdm import tqdm
from seal import tracem as tr
from seal import plotting
import logging

ERROR = 1e-6
logger = logging.getLogger(__name__)


def isSusceptibleSA(
    t: float,
    s: str,
    states,
    events,
    T: float,
    output_signals,
    SAF: int | float,
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


def findDelta(
    signal: str,
    time: float,
    times: list[float],
    simulation: tuple,
    simulation_SA: tuple,
    history: list[str] = [],
    use_masking: bool = True,
) -> tuple[float, set[plotting.Sampling_point], int]:
    """
    Returns:
        - by how much we can proceed
        - what were the sampling points
        - how many samples checked (may be different for sample point size since the latter is a set)
    """
    # if len(history) < 10:
    #     logger.warning("%s:%s", signal, time)

    times_larger = [t for t in times if t > time]
    if len(times_larger) == 0:
        # no more region boundaries ahead -> can proceed as much as wanted
        return float("inf"), {(signal, time)}, 1

    # next region boundary
    end_of_region = min(times_larger)

    # how long to next region boundary
    duration_on_own_signal = end_of_region - time
    ret = [duration_on_own_signal]
    ret_sampling_points: set[plotting.Sampling_point] = {(signal, time)}
    ret_calls: int = 1  # 1 for this call

    if use_masking:
        # check if this event would be masked,
        # i.e., simulation(signal, time) == simulation_SA(signal, time)
        # If so, return
        sim_val = tr.value_at_trace(
            signal=signal, time=time + 2 * ERROR, trace=simulation
        )
        sim_sa_val = tr.value_at_trace(
            signal=signal, time=time + 2 * ERROR, trace=simulation_SA
        )

        assert sim_val != 0.5
        if sim_sa_val == 0.5:
            # assuming these propagate with delay 0
            return ret[0], {(signal, time)}, 1

        if sim_val == sim_sa_val:
            # masking -> do not follow this event anymore
            logger.debug("masking")
            return ret[0], {(signal, time)}, 1

    # Else (i.e., not masked),
    # check recursively on downstream gates
    outputList = tr.getOutputList(signal)
    for output in outputList:
        out_sig = output[0]
        delay = output[1]
        delta, sampling_points, calls = findDelta(
            out_sig,
            time + delay,
            times,
            simulation=simulation,
            simulation_SA=simulation_SA,
            history=history + [f"{signal}:{time}"],
            use_masking=use_masking,
        )
        assert delta > 0
        ret += [delta]
        ret_calls += calls
        ret_sampling_points = ret_sampling_points.union(sampling_points)

    # combine as minimum
    assert min(ret) > 0
    return min(ret), ret_sampling_points, ret_calls


def checkSA(
    times: list[float],
    states: list[tr.State],
    events: list[tr.Event],
    signals: list[str],
    output_signals: list[str],
    snk_delay: float = 10.0,
    src_delay: float = 10.0,
    Textra: float = 30.0,
    exclude_output_signals=True,
    cutoff_min: float = 0.0,
    cutoff_max: float = float("Inf"),
    fault: str = "SA0",
    monitor: bool = False,
    tokens=None,
    input_widths=None,
    output_widths=None,
    victim_signals: list[str] = [],
    plot_sampling_points: bool = False,
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
        init=states[0],
        events=events,
        output_signals=output_signals,
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
        region_idx: int = 0
        region_calls: int = 0
        while tfrom < times[-1]:
            # logger.warning("checking time %s", tfrom)

            # step 0: create simulation with SA
            events_check = events + [
                (tfrom + ERROR, s, SAF),  # add SA0 or SA1
            ]
            simulation_SA = tr.traceSA(
                init=states[0],
                events=events_check,
                output_signals=output_signals,
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
            delta, sampling_points, calls = findDelta(
                signal=s,
                time=tfrom,
                times=times,
                simulation=simulation,
                simulation_SA=simulation_SA,
                use_masking=True,
            )
            mid_point = tfrom + delta / 2

            # for logging, show the sampling points if requested
            if plot_sampling_points:
                plotting.plot(
                    simulation[0],
                    simulation[1],
                    signals,
                    fname=f"{fault}-{s}-{tfrom}-ff.svg",
                    sampling_points=sampling_points,
                )
                plotting.plot(
                    simulation_SA[0],
                    simulation_SA[1],
                    signals,
                    fname=f"{fault}-{s}-{tfrom}-sa.svg",
                    sampling_points=sampling_points,
                )

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

            # sum up calls in this region
            region_calls += calls

            # report & update region index
            if tfrom + delta >= times[region_idx+1]:
                # report
                print(
                    f"Steps for signal {s} for time region {times[region_idx]} to {times[region_idx+1]} = {region_calls}"
                )
                # next region
                region_calls = 0
                region_idx += 1

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
