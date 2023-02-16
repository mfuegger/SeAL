import svgwrite


def points2path(points):
	d = ''
	for i, p in enumerate(points):
		if i == 0:
			d += f'M {p[0]} {p[1]}'
		else:
			d += f'L {p[0]} {p[1]}'

	return d


def plot(times, states, signals, fname='out.svg', dt=10, dv=20, x0=20):
	width = x0 + dt * times[-1]
	height = len(states) * dv
	dwg = svgwrite.Drawing(
		fname,
		size=(height, width),
	)

	signal_ybase = {}
	y = 0
	for s in signals:
		y += dv
		signal_ybase[s] = y
		dwg.add(dwg.text(s, insert=(0,y - dv/2*0.8), font_size="8", fill='black'))
	maxy = y

	for s in states[0].keys():
		ybase = signal_ybase[s]
		points = []
		for i in range(len(times)-1):
			y = ybase - states[i][s] * 0.8 * dv
			if i == 0:
				points += [ (x0 + times[i]*dt, y) ]

			elif len(points) > 0 and points[-1][1] != y:
				points += [ (x0 + times[i]*dt, points[-1][1]), (x0 + times[i]*dt, y) ]

		points += [ (x0 + times[-1]*dt, y) ]

		dwg.add(dwg.path(
			d=points2path(points),
			stroke=svgwrite.rgb(10, 10, 10, '%'),
			fill='white',
			stroke_width=1
		))

	# grid |
	for time in times:
		x = dt*time
		dwg.add(dwg.line(
			(x0 + x, 0), (x0 + x, maxy),
			stroke=svgwrite.rgb(10, 10, 10, '%'),
			stroke_width=0.1
		))
		dwg.add(dwg.text(f'{time}', insert=(x0 + x, maxy + 8), font_size="5", fill='black'))
	maxx = x

	# grid -
	for s in states[0].keys():
		y = signal_ybase[s]
		dwg.add(dwg.line(
			(0, y), (x0 + maxx, y),
			stroke=svgwrite.rgb(10, 10, 10, '%'),
			stroke_width=0.1
		))

	dwg.save()
