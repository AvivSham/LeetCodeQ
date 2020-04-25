from typing import List


def remove_element(nums: List[int], val: int) -> int:
    if val not in nums:
        return len(nums)

    i = 0
    j = len(nums)

    while i < j:
        if nums[i] == val:
            nums.pop(i)
            j = len(nums)
        else:
            i += 1

    return len(nums)


def remove_element_v2(nums: List[int], val: int) -> int:
    while True:
        try:
            nums.remove(val)
        except ValueError:
            break
    return len(nums)


if __name__ == '__main__':
    print(remove_element([3,3], 1))
    print(remove_element_v2([3,3], 3))
