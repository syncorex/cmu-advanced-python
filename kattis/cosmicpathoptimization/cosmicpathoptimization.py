import sys
from typing import List
from math import floor


def average_temps(temps: List[int]) -> int:

    sum = 0
    for temp in temps:
        sum += temp

    return floor(sum / len(temps))


if __name__ == "__main__":
    sys.stdin.readline()
    temps = [int(x) for x in sys.stdin.readline().split()]
    print(average_temps(temps))
