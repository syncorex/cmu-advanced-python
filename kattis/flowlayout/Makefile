PROGRAM = python3
MAIN = flowlayout.py
UNIT_TEST = test_unit_flowlayout.py

all: check_types check_style test unittest clean

test:
	cat 1.in | $(PROGRAM) $(MAIN) | diff - 1.ans
	cat 2.in | $(PROGRAM) $(MAIN) | diff - 2.ans
	cat 3.in | $(PROGRAM) $(MAIN) | diff - 3.ans

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

clean:
	rm -rf __pycache__ .mypy_cache .pytest_cache
