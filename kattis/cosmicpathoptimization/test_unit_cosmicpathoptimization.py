#! /usr/bin/env python3

import unittest

from cosmicpathoptimization import average_temps


class TestCosmicPathOptimization(unittest.TestCase):

    def test1_average_temps(self) -> None:
        temps = [0]
        self.assertEqual(average_temps(temps), 0)

    def test2_calc_slats(self) -> None:
        temps = [10]
        self.assertEqual(average_temps(temps), 10)

    def test3_calc_slats(self) -> None:
        temps = [0, 100]
        self.assertEqual(average_temps(temps), 50)

    def test4_calc_swords(self) -> None:
        temps = [0, 10, 20]
        self.assertEqual(average_temps(temps), 10)

    def test5_calc_swords(self) -> None:
        temps = [125, 362, 24]
        self.assertEqual(average_temps(temps), 170)

    def test6_calc_swords(self) -> None:
        temps = [112, 86, 59]
        self.assertEqual(average_temps(temps), 85)


if __name__ == "__main__":

    unittest.main(verbosity=2)
