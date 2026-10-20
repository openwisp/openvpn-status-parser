.PHONY: clean doc-html doc-clean

PYTHON ?= python3

clean:
	rm -rf dist

doc-html:
	$(PYTHON) -m pip install -e .
	$(PYTHON) -m sphinx -b html docs docs/_build/html

doc-clean:
	rm -rf docs/_build
