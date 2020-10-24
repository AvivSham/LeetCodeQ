from typing import List


def missing_number(nums: List[int]) -> int:
    return(set(range(len(nums) + 1)) - set(nums)).pop()


if __name__ == '__main__':
    numbers = [3, 0, 1]
    print(missing_number(numbers))
