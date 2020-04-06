from typing import List


def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    len_ = len(nums)

    if len_ < 3:
        return max(nums)

    # arr will hold the max rob until to i-position
    arr = [0]*(len_)
    arr[0] = nums[0]
    arr[1] = max(nums[:2])

    for i in range(2, len_):
        # cal formula - take the maximum between the max rob till previous index (i-1) or
        # take the max rob till two previous indexes (i-2) in addition to current rob (i)
        arr[i] = max(arr[i-2]+nums[i], arr[i-1])
    return arr[-1]


if __name__ == '__main__':
    print(rob([2, 7, 9, 3, 1]))
