#! /usr/bin/env python3

import unittest
from typing import List

from pizza2 import cheese_area, pizza_area

class TestPizza(unittest.TestCase):

    def test1_cheese_area(self) -> None:
        self.assertEqual(cheese_area(1, 1), 0)

    def test2_cheese_area(self) -> None:
        self.assertEqual(cheese_area(5, 3), 12.566370614359172)

    def test3_cheese_area(self) -> None:
        with self.assertRaises(Exception):
            cheese_area(3, 4)

    def test4_pizza_area(self) -> None:
        self.assertEqual(pizza_area(0), 0)

    def test5_pizza_area(self) -> None:
        self.assertEqual(pizza_area(3), 28.274333882308138)

    def test6_pizza_area(self) -> None:
        with self.assertRaises(Exception):
            pizza_area(-3)

if __name__ == "__main__":

        unittest.main(verbosity=2)
