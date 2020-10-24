from typing import List
from itertools import combinations


def num_identical_pairs(nums: List[int]) -> int:

    ans = 0
    if len(nums) == len(set(nums)):
        return ans

    for idx in combinations(range(len(nums)), 2):
        if nums[idx[0]] == nums[idx[1]]:
            ans += 1
    return ans
