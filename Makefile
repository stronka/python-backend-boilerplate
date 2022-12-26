PYTHON=pdm run python

install:
	pdm sync

up:
	$(PYTHON) app/main.py

flake8:
	$(PYTHON) -m flake8

pre-commit:
	pre-commit run --all-files
