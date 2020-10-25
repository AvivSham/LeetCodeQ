from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    if len(nums) == 2:
        return nums

    ans = []
    mid = len(nums) // 2
    for i in range(mid):
        ans.append(nums[i])
        ans.append(nums[i + mid])
    return ans