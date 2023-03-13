all: trace-muller-linear.pdf trace-muller-linear-glitch.pdf trace-muller-linear-glitch-ii.pdf trace-muller-linear-check.pdf inv-pdf



inv-pdf: trace-inv.svg trace-inv-glitch.svg trace-inv-glitch-prop.svg
	inkscape trace-inv.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-inv.pdf
	inkscape trace-inv-glitch.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-inv-glitch.pdf
	inkscape trace-inv-glitch-prop.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-inv-glitch-prop.pdf

trace-inv.svg: ../main-inv.py
	python3 ../main-inv.py && cp out.svg trace-inv.svg

trace-inv-glitch.svg: ../main-inv-glitch.py
	python3 ../main-inv-glitch.py && cp out.svg trace-inv-glitch.svg

trace-inv-glitch-prop.svg: ../main-inv-glitch-prop.py
	python3 ../main-inv-glitch-prop.py && cp out.svg trace-inv-glitch-prop.svg



trace-muller-linear.pdf: ../main.py
	python3 ../main.py && cp out.svg trace-muller-linear.svg
	inkscape trace-muller-linear.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-muller-linear.pdf

trace-muller-linear-glitch.pdf: ../main-muller-linear-glitch.py
	python3 ../main-muller-linear-glitch.py && cp out.svg trace-muller-linear-glitch.svg
	inkscape trace-muller-linear-glitch.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-muller-linear-glitch.pdf

trace-muller-linear-glitch-ii.pdf: ../main-muller-linear-glitch-ii.py
	python3 ../main-muller-linear-glitch-ii.py && cp out.svg trace-muller-linear-glitch-ii.svg
	inkscape trace-muller-linear-glitch-ii.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-muller-linear-glitch-ii.pdf

trace-muller-linear-check.pdf: ../main-check.py
	python3 ../main-check.py && cp out.svg trace-muller-linear-check.svg
	inkscape trace-muller-linear-check.svg --export-area-drawing --batch-process --export-type=pdf --export-filename=trace-muller-linear-check.pdf



clean:
	rm *.pdf *.svg