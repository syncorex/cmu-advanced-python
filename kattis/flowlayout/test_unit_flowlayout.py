#! /usr/bin/env python3

import unittest
from typing import List

from flowlayout import window_dims

class TestFlowLayout(unittest.TestCase):
  
    def test1_window_dims(self) -> None:
        max_width = 35
        planks = [(24, 10), (11, 15), (14, 5), (-1, -1)]
        self.assertEqual(window_dims(max_width, planks), (35, 20))

    def test2_window_dims(self) -> None:
        max_width = 20
        planks = [(0, 0), (0, 0), (-1, -1)]
        self.assertEqual(window_dims(max_width, planks), (0, 0))

    def test3_window_dims(self) -> None:
        max_width = 100
        planks = [(120, 12), (0, 0), (-1, -1)]
        self.assertEqual(window_dims(max_width, planks), (120, 12))
    
    def test4_window_dims(self) -> None:
        max_width = 100
        planks = [(100, 1), (0, 2), (-1, -1)]
        self.assertEqual(window_dims(max_width, planks), (100, 2))

    def test5_window_dims(self) -> None:
        max_width = -1
        planks = [(100, 1), (0, 2), (-1, -1)]
        with self.assertRaises(Exception):
            window_dims(max_width, planks)

    def test6_window_dims(self) -> None:
        max_width = 22
        planks = [(-100, 1), (0, 2), (-1, -1)]
        with self.assertRaises(Exception):
            window_dims(max_width, planks)

if __name__ == "__main__":
        
        unittest.main(verbosity=2)
