all: trace.svg
	inkscape trace.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace.pdf

trace.svg:
	python3 ../main.py && cp out.svg trace.svg

clean:
	rm *.pdf *.svg