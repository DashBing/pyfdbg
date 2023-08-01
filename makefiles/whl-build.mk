make := make
ifeq ($(OS),Windows_NT)
	mv := move
	python := python
else
	mv := mv
	python := python3
endif

#all:
#	$(make) build
#	$(make) upload

build:
	$(python) -m build

init:
	$(python) -m pip install -U build
	$(python) -m pip install -U twine
