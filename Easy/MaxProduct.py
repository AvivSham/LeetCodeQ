from typing import List


def max_product(nums: List[int]) -> int:
    if len(nums) == 2:
        return (nums[0] - 1) * (nums[1] - 1)

    nums = sorted(nums)
    return (nums.pop() - 1) * (nums.pop() - 1)


if __name__ == '__main__':
    print(max_product([1, 2, 5, 346, 11, 2, 41]))
