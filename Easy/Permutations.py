from typing import List
from itertools import permutations


def permute(nums: List[int]) -> List[List[int]]:
    return list(permutations(nums, len(nums)))


if __name__ == '__main__':
    print(permute([1, 2, 3, 4]))
