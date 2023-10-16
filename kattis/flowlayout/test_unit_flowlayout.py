#! /usr/bin/env python3

import unittest
from typing import List

from brokenswords import calc_slats, calc_swords

class TestBrokenSwords(unittest.TestCase):
  
    def test1_window_dims(self) -> None:
        slats = ["0000"]
        self.assertEqual(window_dims(slats), (2, 2))

    def test2_window_dims(self) -> None:
        slats = ["1111", "1111"]
        self.assertEqual(window_dims(slats), (0, 0))

    def test3_window_dims(self) -> None:
        slats = ["1100", "0100", "1000"]
        self.assertEqual(window_dims(slats), (2, 6))
    
    def test4_calc_swords(self) -> None:
        v, h = (0, 0)
        self.assertEqual(calc_swords(v, h), (0, 0, 0))

    def test5_calc_swords(self) -> None:
        v, h = (2, 3)
        self.assertEqual(calc_swords(v, h), (1, 0, 1))

    def test6_calc_swords(self) -> None:
        v, h = (11, 17)
        self.assertEqual(calc_swords(v, h), (5, 1, 7))


if __name__ == "__main__":
        
        unittest.main(verbosity=2)
