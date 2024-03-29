## Makefile for Sphinx documentation

## You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
BUILDDIR      = _build
OPENCMD       = $(shell which browse open)

## User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

## Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d ../$(BUILDDIR)/doctrees $(SPHINXOPTS) .
## the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html        to make standalone HTML files of Hippo User Guide"

.PHONY: clean
clean:
	@rm -rf $(BUILDDIR)/html/*
	@rm -rf $(BUILDDIR)/doctrees/*
	@echo "Remove build directory."

.PHONY: html
html:
	@cd ./src && $(SPHINXBUILD) -b html $(ALLSPHINXOPTS) ../$(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in ../$(BUILDDIR)/html."

.PHONY: run
run:
	@echo "Open static website."
	@$(word 1, $(OPENCMD)) "$(BUILDDIR)/html/index.html"
