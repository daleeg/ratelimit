PYTHON ?= python3

dist: clean
	$(PYTHON) setup.py sdist bdist_wheel

clean:
	-rm -r build dist pyratelimit.egg-info

pypi:
	twine upload  dist/*