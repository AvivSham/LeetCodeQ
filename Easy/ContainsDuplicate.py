from typing import List
from collections import Counter


def contains_duplicate(nums: List[int]) -> bool:
    if len(nums) < 2:
        return False

    return False if len(set(nums)) == len(nums) else True


def contains_duplicate_v2(nums: List[int]) -> bool:
    if len(nums) < 2:
        return False

    for i in Counter(nums).values():
        if i != 1:
            return True
    return False


if __name__ == '__main__':
    print(contains_duplicate_v2( [1,2,3,1]))
    print(contains_duplicate_v2([1,2,3,4]))
    print(contains_duplicate_v2([1,1,1,3,3,4,3,2,4,2]))
