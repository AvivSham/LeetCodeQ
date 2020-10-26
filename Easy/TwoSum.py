from typing import List


def twosum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        if target - nums[i] in nums[i+1:]:
            return [i, i+1+nums[i+1:].index(target - nums[i])]


if __name__ == '__main__':
    print(twosum([3, 2, 4], 6))