import sys
import math

def cheese_area(r:int, c:int) -> float:
    return math.pi * (r-c)**2

def pizza_area(r:int) -> float:
    return (math.pi * r**2)

if __name__ == "__main__":
    r, c = list(map(lambda x: int(x), sys.stdin.readline().split()))
    print(cheese_area(r, c) / pizza_area(r) * 100)