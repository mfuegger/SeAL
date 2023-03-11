all: trace.svg trace-glitch.svg trace-glitch-ii.svg trace-check.svg trace-inv.svg trace-inv-glitch.svg trace-inv-glitch-prop.svg
	inkscape trace.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace.pdf
	inkscape trace-glitch.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-glitch.pdf
	inkscape trace-check.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-check.pdf
	inkscape trace-glitch-ii.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-glitch-ii.pdf
	inkscape trace-inv.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-inv.pdf
	inkscape trace-inv-glitch.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-inv-glitch.pdf
	inkscape trace-inv-glitch-prop.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-inv-glitch-prop.pdf


trace-inv.svg: ../main-inv.py
	python3 ../main-inv.py && cp out.svg trace-inv.svg

trace-inv-glitch.svg: ../main-inv-glitch.py
	python3 ../main-inv-glitch.py && cp out.svg trace-inv-glitch.svg

trace-inv-glitch-prop.svg: ../main-inv-glitch-prop.py
	python3 ../main-inv-glitch-prop.py && cp out.svg trace-inv-glitch-prop.svg


trace.svg: ../main.py
	python3 ../main.py && cp out.svg trace.svg

trace-glitch.svg: ../main-glitch.py
	python3 ../main-glitch.py && cp out.svg trace-glitch.svg

trace-glitch-ii.svg: ../main-glitch-ii.py
	python3 ../main-glitch-ii.py && cp out.svg trace-glitch-ii.svg

trace-check.svg: ../main-check.py
	python3 ../main-check.py && cp out.svg trace-check.svg

clean:
	rm *.pdf *.svg