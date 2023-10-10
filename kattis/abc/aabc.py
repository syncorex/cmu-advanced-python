import sys
from typing import List

def answer(nums:List[int], order:str) -> str:
    nums.sort()
    result = ['', '', '']
    for i in range(3):
        j = ord(order[i])-65
        result[i] = str(nums[j])
    return ' '.join(result)

if __name__ == "__main__":
    nums = [int(x) for x in sys.stdin.readline().split()]
    order = sys.stdin.readline()
    print(answer(nums, order))
