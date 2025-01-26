import svgwrite
import matplotlib.pyplot as plt
from seal import tracem as tr

Point = tuple[float, float]
Sampling_point = tuple[str, float]


def points2path(points: list[Point]) -> str:
    d = ""
    for i, p in enumerate(points):
        if i == 0:
            d += f"M {p[0]} {p[1]}"
        else:
            d += f"L {p[0]} {p[1]}"
    return d


def plotSensitivityBars(p_per_sig, fname: str = "bar.pdf", title=None) -> None:
    fig = plt.figure(figsize=(6.5, 4))

    if title is not None:
        plt.title(title, fontsize=35)

    x = p_per_sig.keys()
    height = p_per_sig.values()
    plt.bar(x, height, width=0.8)
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)

    plt.savefig(fname, dpi=300, pad_inches=1.1)


def plot(
    times: list[float],
    states: list[tr.State],
    signals: list[str],
    init=None,
    events=None,
    delays=None,
    fname="out.svg",
    dt: float = 30.0,
    dv: float = 60.0,
    x0: float = 60.0,
    susceptible=None,
    fault="SET",
    cutoff=None,
    sampling_points: set[Sampling_point] = set(),
):
    GRID_COLOR = svgwrite.rgb(30, 30, 30, "%")
    GRID_LW = 0.1

    SIGNAL_LW = 4

    width = x0 + dt * times[-1]
    height = len(states[0]) * dv + 200
    dwg = svgwrite.Drawing(
        fname,
        size=(width + 40, height),
    )

    signal_ybase = {}
    y = 0.0
    for s in signals:
        y += dv
        signal_ybase[s] = y
        dwg.add(dwg.text(s, insert=(0, y - dv / 2 * 0.8), font_size="16", fill="black"))
    maxy = y

    for s in states[0].keys():
        ybase = signal_ybase[s]

        # make points
        points = []
        for i in range(len(times)):
            y = ybase - states[i][s] * 0.8 * dv

            # get points for signal line
            if i == 0:
                points += [(x0 + times[i] * dt, y)]

            elif len(points) > 0 and points[-1][1] != y:
                points += [(x0 + times[i] * dt, points[-1][1]), (x0 + times[i] * dt, y)]

        points += [(x0 + times[-1] * dt, y)]

        # make patches
        patches = []
        previous_state = None
        patch_M_start = None
        for i in range(len(times)):
            if (patch_M_start is not None) and (i == len(times) - 1):
                # M patch is open and end of time
                patches += [(patch_M_start, times[i])]
                patch_M_start = None

            # get patches for M
            elif states[i][s] != previous_state:
                # state change
                if states[i][s] == 0.5:
                    # start of an M
                    patch_M_start = times[i]

                elif (patch_M_start is not None) and (states[i][s] != 0.5):
                    # end of M patch
                    patches += [(patch_M_start, times[i])]
                    patch_M_start = None

            previous_state = states[i][s]

        # draw points
        dwg.add(
            dwg.path(
                d=points2path(points),
                stroke=svgwrite.rgb(10, 10, 10, "%"),
                fill="white",
                stroke_width=SIGNAL_LW,
            )
        )

        # draw patches
        for patch in patches:
            dwg.add(
                dwg.rect(
                    (x0 + patch[0] * dt, ybase - 0.8 * dv),
                    (patch[1] * dt - patch[0] * dt, 0.8 * dv),
                    stroke="red",
                    fill="red",
                    opacity=0.5,
                    stroke_width=3,
                )
            )

    # grid |
    x = 0.0
    last_annotated_time = float("-inf")
    for i, time in enumerate(times):
        x = dt * time
        dwg.add(
            dwg.line(
                (x0 + x, 0), (x0 + x, maxy), stroke=GRID_COLOR, stroke_width=GRID_LW
            )
        )
        if i == 0 or (i > 0 and time - last_annotated_time > 0.5):
            last_annotated_time = time
            # only annotate times that are not too close to previous times
            if time == int(time):
                time = int(time)
            dwg.add(
                dwg.text(
                    f"{time}", insert=(x0 + x, maxy + 16), font_size="12", fill="black"
                )
            )
    maxx = x

    # grid -
    for s in states[0].keys():
        y = signal_ybase[s]
        dwg.add(
            dwg.line((0, y), (x0 + maxx, y), stroke=GRID_COLOR, stroke_width=GRID_LW)
        )

    # potentially add susceptible signal regions
    # if susceptible is not None:
    # 	if fault == 'SA0':
    # 		stroke_color = 'purple'
    # 		fill_color = 'purple'
    # 	elif fault == 'SA1':
    # 		stroke_color = 'green'
    # 		fill_color = 'green'
    # 	else:
    # 		stroke_color = 'blue'
    # 		fill_color = 'blue'

    # 	for (s,interval) in susceptible:
    # 		yfrom = signal_ybase[s]
    # 		xfrom = x0 + dt*interval[0]
    # 		xto = x0 + dt*interval[1]
    # 		dwg.add(dwg.rect(
    # 			(xfrom,  yfrom - 0.8 * dv),
    # 			(xto - xfrom, 0.8 * dv),
    # 			stroke=stroke_color,
    # 			fill=fill_color,
    # 			opacity=0.1,
    # 			stroke_width=0
    # 		))

    # potentially add susceptible signal regions
    if susceptible is not None:
        if fault == "SET":
            stroke_color = "blue"
            fill_color = "blue"

            for s, interval in susceptible:
                yfrom = signal_ybase[s]
                xfrom = x0 + dt * interval[0]
                xto = x0 + dt * interval[1]
                dwg.add(
                    dwg.rect(
                        (xfrom, yfrom - 0.8 * dv),
                        (xto - xfrom, 0.8 * dv),
                        stroke=stroke_color,
                        fill=fill_color,
                        opacity=0.1,
                        stroke_width=0,
                    )
                )

        else:
            for s in susceptible:
                for sig, interval, SAF in s:
                    yfrom = signal_ybase[sig]
                    xfrom = x0 + dt * interval[0]
                    xto = x0 + dt * interval[1]

                    if SAF == "SA0":
                        stroke_color = "purple"
                        fill_color = "purple"
                    elif SAF == "SA1":
                        stroke_color = "green"
                        fill_color = "green"
                    else:
                        raise ValueError("cannot plot this")

                    dwg.add(
                        dwg.rect(
                            (xfrom, yfrom - 0.8 * dv),
                            (xto - xfrom, 0.8 * dv),
                            stroke=stroke_color,
                            fill=fill_color,
                            opacity=0.1,
                            stroke_width=0,
                        )
                    )

    # potentially draw cutoff boundaries
    if cutoff is not None:
        # is of form [min, max]
        if cutoff[0] > 0:
            time = cutoff[0]
            x = dt * time
            dwg.add(
                dwg.line(
                    (x0 + x, 0),
                    (x0 + x, maxy + 1),
                    stroke=svgwrite.rgb(70, 70, 70, "%"),
                    stroke_width=2,
                    stroke_dasharray=5,
                )
            )

        if cutoff[1] < times[-1]:
            time = cutoff[1]
            x = dt * time
            dwg.add(
                dwg.line(
                    (x0 + x, 0),
                    (x0 + x, maxy + 1),
                    stroke=svgwrite.rgb(70, 70, 70, "%"),
                    stroke_width=2,
                    stroke_dasharray=5,
                )
            )

    # draw sampling points
    stroke_color = "blue"
    fill_color = "blue"
    for point in sampling_points:
        x = x0 + dt * point[1]
        y = signal_ybase[point[0]]
        dwg.add(
            dwg.circle(
                (x, y),
                r=7.0,
                stroke=stroke_color,
                fill=fill_color,
                opacity=0.5,
                stroke_width=0,
            )
        )

    # print circuit parameters
    if delays is not None:
        text_block_init = f"Init: {init}"
        text_block_events = "\t".join([f"{event}" for event in events])
        text_block_delays = f"Delays: {delays}"

        # Adjust the text insertion point to avoid overlap
        text_y_position = maxy + 70
        dwg.add(
            dwg.text(
                text_block_init,
                insert=(20, text_y_position),
                font_size="16",
                fill="black",
            )
        )
        text_y_position += 20
        dwg.add(
            dwg.text(
                "Events:", insert=(20, text_y_position), font_size="16", fill="black"
            )
        )
        text_y_position += 20
        for line in text_block_events.split("\n"):
            dwg.add(
                dwg.text(
                    line, insert=(20, text_y_position), font_size="16", fill="black"
                )
            )
            text_y_position += 20
        dwg.add(
            dwg.text(
                text_block_delays,
                insert=(20, text_y_position),
                font_size="16",
                fill="black",
            )
        )
        text_y_position += 20

    dwg.save()
