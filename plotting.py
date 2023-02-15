import svgwrite


def plot(times, states, fname='out.svg', dt=10):
	dwg = svgwrite.Drawing(fname)

	signal_ybase = {}
	y = 0
	for s in states[0].keys():
		y += 10
		signal_ybase[s] = y

	for s in states[0].keys():
		ybase = signal_ybase[s]
		points = []
		for i in range(len(times)-1):
			y = ybase + states[i][s] * 8.0
			if i == 0:
				points += [ (times[i], y) ]

			elif len(points) > 0 and points[-1][1] != y:
				points += [ (times[i]*dt, points[-1][1]), (times[i]*dt, y) ]

		points += [ (times[-1]*dt, y) ]

		for i in range(len(points)-1):
			dwg.add(dwg.line(points[i], points[i+1], stroke=svgwrite.rgb(10, 10, 10, '%')))

	dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
	dwg.save()