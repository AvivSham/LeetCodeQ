from typing import List


def minsubsequence(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return nums

    nums = sorted(nums)
    ans = []
    for _ in range(len(nums)):
        ans.append(nums.pop())
        if sum(ans) > sum(nums):
            return ans


if __name__ == '__main__':
    print(minsubsequence([4, 4, 7, 6, 7]))
