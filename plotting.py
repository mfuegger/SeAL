import svgwrite


def points2path(points):
	d = ''
	for i, p in enumerate(points):
		if i == 0:
			d += f'M {p[0]} {p[1]}'
		else:
			d += f'L {p[0]} {p[1]}'

	return d


def plot(times, states, signals, fname='out.svg', dt=30, dv=60, x0=60, susceptible=None, cutoff=None):
	width = x0 + dt * times[-1]
	height = len(states[0]) * dv + 200
	dwg = svgwrite.Drawing(
		fname,
		size=(width + 40, height),
	)

	signal_ybase = {}
	y = 0
	for s in signals:
		y += dv
		signal_ybase[s] = y
		dwg.add(dwg.text(s, insert=(0,y - dv/2*0.8), font_size="16", fill='black'))
	maxy = y

	for s in states[0].keys():
		ybase = signal_ybase[s]
		
		# make points
		points = []
		for i in range(len(times)):
			y = ybase - states[i][s] * 0.8 * dv

			# get points for signal line
			if i == 0:
				points += [ (x0 + times[i]*dt, y) ]

			elif len(points) > 0 and points[-1][1] != y:
				points += [ (x0 + times[i]*dt, points[-1][1]), (x0 + times[i]*dt, y) ]

		points += [ (x0 + times[-1]*dt, y) ]

		# make patches
		patches = []
		previous_state = None
		patch_M_start = None
		for i in range(len(times)):
			if (patch_M_start is not None) and ( i == len(times)-1 ):
					# M patch is open and end of time
					patches += [ (patch_M_start, times[i]) ]
					patch_M_start = None

			# get patches for M
			elif states[i][s] != previous_state:
				# state change
				if states[i][s] == 0.5:
					# start of an M
					patch_M_start = times[i]

				elif (patch_M_start is not None) and (states[i][s] != 0.5):
					# end of M patch
					patches += [ (patch_M_start, times[i]) ]
					patch_M_start = None

			previous_state = states[i][s]

		# draw points
		dwg.add(dwg.path(
			d=points2path(points),
			stroke=svgwrite.rgb(10, 10, 10, '%'),
			fill='white',
			stroke_width=3
		))

		# draw patches
		for patch in patches:
			dwg.add(dwg.rect(
				(x0 + patch[0]*dt, ybase - 0.8 * dv),
				(patch[1]*dt - patch[0]*dt, 0.8 * dv),
				stroke='red',
				fill='red',
				opacity=0.5,
				stroke_width=3
			))

	# grid |
	for i, time in enumerate(times):
		x = dt*time
		dwg.add(dwg.line(
			(x0 + x, 0), (x0 + x, maxy),
			stroke=svgwrite.rgb(10, 10, 10, '%'),
			stroke_width=0.3
		))
		if i == 0 or ( i > 0 and time - times[i-1] > 0.25 ):
			# only annotate times that are not too close to previous times
			dwg.add(dwg.text(f'{time}', insert=(x0 + x, maxy + 16), font_size="12", fill='black'))
	maxx = x

	# grid -
	for s in states[0].keys():
		y = signal_ybase[s]
		dwg.add(dwg.line(
			(0, y), (x0 + maxx, y),
			stroke=svgwrite.rgb(10, 10, 10, '%'),
			stroke_width=0.3
		))

	# potentially add susceptible signal regions
	if susceptible is not None:
		for (s,interval) in susceptible:
			yfrom = signal_ybase[s]
			xfrom = x0 + dt*interval[0]
			xto = x0 + dt*interval[1]
			dwg.add(dwg.rect(
				(xfrom,  yfrom - 0.8 * dv),
				(xto - xfrom, 0.8 * dv),
				stroke='blue',
				fill='blue',
				opacity=0.1,
				stroke_width=0
			))

	# potentially draw cutoff boundaries
	if cutoff is not None:
		# is of form [min, max]
		if cutoff[0] > 0:
			time = cutoff[0]
			x = dt*time
			dwg.add(dwg.line(
				(x0 + x, 0), (x0 + x, maxy + 1),
				stroke=svgwrite.rgb(70, 70, 70, '%'),
				stroke_width=2,
				stroke_dasharray=5
			))

		if cutoff[1] < times[-1]:
			time = cutoff[1]
			x = dt*time
			dwg.add(dwg.line(
				(x0 + x, 0), (x0 + x, maxy + 1),
				stroke=svgwrite.rgb(70, 70, 70, '%'),
				stroke_width=2,
				stroke_dasharray=5
			))

	dwg.save()
