PROGRAM = python3
MAIN = cosmicpathoptimization.py
UNIT_TEST = test_unit_cosmicpathoptimization.py

all: check_types check_style fix_style test unittest kattis clean

test:
	cat data/1.in | $(PROGRAM) $(MAIN) | diff - data/1.ans

check_types:
ifeq ($(shell which mypy), ) # if mypy not found
	@echo "mypy not found. Installing..."
	pip install mypy
endif
	mypy --disallow-untyped-defs --strict $(MAIN)

unittest:
ifeq ($(shell which pytest), ) # if pytest not found
	@echo "pytest not found. Installing..."
	pip install pytest
endif
	pytest $(UNIT_TEST)

check_style:
ifeq ($(shell which flake8), ) # if flake8 not found
	@echo "flake8 not found. Installing..."
	pip install flake8
endif
	flake8 $(MAIN) --count --show-source --statistics
	flake8 $(UNIT_TEST) --count --show-source --statistics

fix_style:
ifeq ($(shell which autopep8), ) # if autopep not found
	@echo "autopep8 not found, installing..."
	pip install autopep8
endif
	autopep8 --in-place --aggressive --aggressive $(MAIN)
	autopep8 --in-place --aggressive --aggressive $(UNIT_TEST)

kattis:
	kattis $(MAIN)

clean:
	rm -rf __pycache__ .mypy_cache .pytest_cache
