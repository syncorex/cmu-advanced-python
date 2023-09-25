import sys
from typing import List

def desired_order(nums:List[int], order:str) -> str:
    nums.sort()
    result = ['', '', '']
    for i in range(3):
        j = ord(order[i])-65
        result[i] = str(nums[j])
    return ' '.join(result)

if __name__ == "__main__":
    nums = list(map(lambda x: int(x), sys.stdin.readline().split()))
    order = sys.stdin.readline()
    print(desired_order(nums, order))
