from typing import List
from collections import Counter


# solution without using collections
def single_number(nums: List[int]) -> int:
    # checking edge cases
    if len(nums) == 1:
        return nums[0]

    nums = sorted(nums)

    if nums[0] != nums[1]:
        return nums[0]

    if nums[-1] != nums[-2]:
        return nums[-1]

    # core
    for i in range(2, len(nums) - 1):
        if (nums[i] != nums[i - 1]) and (nums[i] != nums[i + 1]):
            return nums[i]


# solution using collections
def single_number_ver2(nums: List[int]) -> int:
    for item in Counter(nums).items():
        if item[1] == 1:
            return item[0]


if __name__ == '__main__':
    print(single_number([4, 1, 2, 1, 2]))
    print(single_number_ver2([4, 1, 2, 1, 2]))
