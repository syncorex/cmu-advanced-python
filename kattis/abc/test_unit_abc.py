#! /usr/bin/env python3

import unittest
from typing import List

from aabc import answer

class TestABC(unittest.TestCase):
  
    def test1_answer(self) -> None:
        nums = [7, 2, 4]
        order = "CBA"
        self.assertEqual(answer(nums, order), "7 4 2")
    
    def test2_answer(self) -> None:
        nums = [1, 2, 30]
        order = "BAC"
        self.assertEqual(answer(nums, order), "2 1 30")
    
    def test3_answer(self) -> None:
        nums = [10, 2, 7]
        order = "ACB"
        self.assertEqual(answer(nums, order), "2 10 7")

    def test4_type(self) -> None:
        self.assertEqual(answer("sdfk", [2,3,4]), "hello")
    
    def neg_int_count(self, temps:List[int]) -> int:
        neg_count = 0
        for n in temps:
            if n < 0:
                neg_count += 1
        return neg_count

if __name__ == "__main__":
        unittest.main(verbosity=2)
