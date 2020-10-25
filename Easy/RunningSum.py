from typing import List


def running_sum(nums: List[int]) -> List[int]:
    if len(nums) == 1:
        return [nums[0]]

    ans = [nums[0]]
    for i in range(1, len(nums)):
        ans.append(ans[-1] + nums[i])
    return ans


if __name__ == '__main__':
    nums_list = [3, 1, 2, 10, 1]
    print(running_sum(nums_list))
