#!/bin/bash
pdflatex --draft --shell-escape lecture-notes
makeindex lecture-notes
pdflatex --shell-escape lecture-notes
