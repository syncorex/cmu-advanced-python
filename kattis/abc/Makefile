PROGRAM = python3
MAIN = aabc.py

all: check_types check_style test unittest clean

test:
	cat 1.in | $(PROGRAM) $(MAIN) | diff - 1.ans

check_types:
	mypy --disallow-untyped-defs --strict aabc.py

unittest:
ifeq ($(shell which pytest), ) # if pytest not found
	@echo "pytest not found. Installing..."
	pip install pytest
endif
	pytest test_unit_abc.py

check_style:
	flake8 aabc.py --count --show-source --statistics

clean:
	rm -rf __pycache__ .mypy_cache .pytest_cache
