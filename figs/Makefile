all: trace.svg trace-glitch.svg trace-glitch-ii.svg trace-check.svg
	inkscape trace.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace.pdf
	inkscape trace-glitch.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-glitch.pdf
	inkscape trace-check.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-check.pdf
	inkscape trace-glitch-ii.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-glitch-ii.pdf

trace.svg: ../main.py
	python3 ../main.py && cp out.svg trace.svg

trace-glitch.svg: ../main-glitch.py
	python3 ../main-glitch.py && cp out.svg trace-glitch.svg

trace-glitch.svg: ../main-glitch-ii.py
	python3 ../main-glitch-ii.py && cp out.svg trace-glitch-ii.svg

trace-check.svg: ../main-check.py
	python3 ../main-check.py && cp out.svg trace-check.svg

clean:
	rm *.pdf *.svg