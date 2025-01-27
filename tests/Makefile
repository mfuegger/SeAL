clean:
	rm -f *.svg *.pdf

figures: clean buf_MCE2_case0.pdf buf_MCE2_case1.pdf buf_MCE2_regions.pdf feedbackMCE2_regions.pdf

buf_MCE2_case0.pdf:
	python3 buf_MCE2.py --runtime=15 --testcase=0
	inkscape --export-filename=buf_MCE2.pdf buf_MCE2.svg
	pdfcrop --margins '5 5 5 5' --clip buf_MCE2.pdf buf_MCE2_case0.pdf

buf_MCE2_case1.pdf:
	python3 buf_MCE2.py --runtime=15 --testcase=1
	inkscape --export-filename=buf_MCE2.pdf buf_MCE2.svg
	pdfcrop --margins '5 5 5 5' --clip buf_MCE2.pdf buf_MCE2_case1.pdf

buf_MCE2_regions.pdf:
	python3 buf_MCE2.py --runtime=25 --delta2
	inkscape --export-filename=buf_MCE2.pdf buf_MCE2.svg
	pdfcrop --margins '5 5 5 5' --clip buf_MCE2.pdf buf_MCE2_regions.pdf

feedbackMCE2_regions.pdf:
	python3 feedbackMCE2.py --runtime=40 --delta2
	inkscape --export-filename=feedbackMCE2.pdf feedbackMCE2.svg
	pdfcrop --margins '5 5 5 5' --clip feedbackMCE2.pdf feedbackMCE2_regions.pdf