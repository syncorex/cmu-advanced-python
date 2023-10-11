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
        nums = [70, 3, 2]
        order = "ABC"
        self.assertEqual(answer(nums, order), "2 3 70")

    def test3_answer(self) -> None:
        nums = [1, 2, 30]
        order = "BAC"
        self.assertEqual(answer(nums, order), "2 1 30")
    
    def test4_answer(self) -> None:
        nums = [10, 2, 7]
        order = "ACB"
        self.assertEqual(answer(nums, order), "2 10 7")

    def test5_type(self) -> None:
        nums = "sdfk"
        order = "ABC"
        with self.assertRaises(AttributeError):
            answer(nums, order)

    def test6_type(self) -> None:
        nums = [1, 2, 3]
        order = 10
        with self.assertRaises(TypeError):
            answer(nums, order)
    
if __name__ == "__main__":
        
        unittest.main(verbosity=2)
