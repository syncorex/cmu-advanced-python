import sys
from typing import List, Tuple


def calc_slats(swords: List[str]) -> Tuple[int, int]:

    v_slats = 0
    h_slats = 0

    for sword in swords:
        for i in range(2):
            if sword[i] == "0":
                v_slats += 1
        for i in range(2, 4):
            if sword[i] == "0":
                h_slats += 1

    return (v_slats, h_slats)


def calc_swords(v_slats: int, h_slats: int) -> Tuple[int, int, int]:

    swords = 0

    while (v_slats > 1 and h_slats > 1):
        swords += 1
        v_slats -= 2
        h_slats -= 2

    return (swords, v_slats, h_slats)


if __name__ == "__main__":

    sys.stdin.readline()
    lines = sys.stdin.readlines()
    v, h = calc_slats(lines)
    swords, v_left, h_left = calc_swords(v, h)
    print(swords, v_left, h_left)
