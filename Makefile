.PHONY: build clean doc-html doc-clean

PYTHON ?= python3

build:
	$(PYTHON) setup.py sdist bdist_wheel

clean:
	rm -rf dist

doc-html:
	$(PYTHON) -m pip install -e .
	$(PYTHON) -m sphinx -b html docs docs/_build/html

doc-clean:
	$(MAKE) -C docs clean
