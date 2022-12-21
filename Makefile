PYTHON=python2.7
BIBTEX=bibtex
JEKYLL=jekyll

# targets that aren't filenames
.PHONY: all clean deploy

all: cv  _site/index.html

BUILDARGS :=

_includes/pubs.html: bib/pubs.bib bib/publications.tmpl
	mkdir -p _includes
	$(PYTHON) bibble/bibble.py $+ > $@

_site/index.html: $(wildcard *.html) _config.yml \
	_layouts/default.html
	$(JEKYLL) build

cv: cv/cv.tex
	$(MAKE) -C cv

clean:
	$(RM) -r _site
	$(MAKE) -C cv clean

deploy: clean all
