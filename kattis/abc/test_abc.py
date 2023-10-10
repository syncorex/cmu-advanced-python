#!/ usr/bin/env python3

__author__ = "Zeke Barefoot"
__copyright__ = "Copyright 2023"
__license__ = "MIT"

from aabc import answer

def test_answer():
  assert answer([1, 2, 3], "CBA") == "3 2 1"
  assert answer([6, 4, 2], "BAC") == "4 2 6"
  assert answer([8, 3, 5], "ACB") == "3 8 5"
  print('All functional tests passed')

if __name__ == "__main__":
  test_answer()