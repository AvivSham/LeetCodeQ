from typing import List


def min_start_value(nums: List[int]) -> int:
    t = 0
    m = float('inf')

    for i in nums:
        m = min(m, t)
        t += i

    return abs(min(m, t)) + 1


if __name__ == '__main__':
    n = [-3, 2, -3, 4, 2]
    print(min_start_value(n))
