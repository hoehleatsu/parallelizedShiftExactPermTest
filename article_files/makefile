main=main

all: ${main}.pdf supplement.pdf coverletter.pdf in_brief.pdf

%.pdf: %.tex sample.bib
	pdflatex -shell-escape $*.tex
	if ( grep -q citation $*.aux ) ; then \
		bibtex $* ; \
		pdflatex -shell-escape $*.tex ; \
	fi
	pdflatex -shell-escape $*.tex
	#latex $*.tex
	#dvipdfm $*.dvi

diff.tex: ${main}.tex
	git show quandenser_mcp_2:./$? > /tmp/$?
	latexdiff /tmp/$? $? > diff.tex

clean:
	rm -f *.aux *.bbl *.blg *.log *~
