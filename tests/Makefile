figures: clean buf_MCE2_case0.pdf buf_MCE2_case1.pdf buf_MCE2_regions.pdf feedbackMCE2_regions.pdf buf_MCE2_affected_nomasking.pdf feedbackMCE2_affected_nomasking.pdf

clean:
	rm -f *.svg *.pdf

buf_MCE2_case0.pdf:
	python3 buf_MCE2.py --runtime=15 --testcase=0
	inkscape --export-filename=buf_MCE2.pdf buf_MCE2.svg
	pdfcrop --margins '5 5 5 5' --clip buf_MCE2.pdf buf_MCE2_case0.pdf

buf_MCE2_case1.pdf:
	python3 buf_MCE2.py --runtime=15 --testcase=1
	inkscape --export-filename=buf_MCE2.pdf buf_MCE2.svg
	pdfcrop --margins '5 5 5 5' --clip buf_MCE2.pdf buf_MCE2_case1.pdf

buf_MCE2_regions.pdf:
	python3 buf_MCE2.py --runtime=21 --delta2
	inkscape --export-filename=buf_MCE2.pdf buf_MCE2.svg
	pdfcrop --margins '5 5 5 5' --clip buf_MCE2.pdf buf_MCE2_regions.pdf

feedbackMCE2_regions.pdf:
	python3 feedbackMCE2.py --runtime=40 --delta2
	inkscape --export-filename=feedbackMCE2.pdf feedbackMCE2.svg
	pdfcrop --margins '5 5 5 5' --clip feedbackMCE2.pdf feedbackMCE2_regions.pdf

feedbackMCE2_affected_nomasking.pdf:
	python3 feedbackMCE2.py --runtime=40 --delta2 --plotaffectedpoints --nomasking
	inkscape --export-filename=feedbackMCE2.pdf SA1-a-0.0-ff.svg
	pdfcrop --margins '5 5 5 5' --clip feedbackMCE2.pdf feedbackMCE2_affected_nomasking.pdf

buf_MCE2_affected_nomasking.pdf:
	python3 buf_MCE2.py --runtime=21 --delta2 --plotaffectedpoints --nomasking
	inkscape --export-filename=buf_MCE2.pdf SA1-b1-0.0-ff.svg
	pdfcrop --margins '5 5 5 5' --clip buf_MCE2.pdf buf_MCE2_affected_nomasking.pdf