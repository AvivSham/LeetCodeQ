from typing import List


def smallestrange(A: List[int], K: int) -> int:
    max_num, min_num = max(A), min(A)
    diff, extension = max_num - min_num, 2 * K

    if diff <= extension:
        return 0

    else:
        return diff - extension


if __name__ == '__main__':
    print(smallestrange([1, 3, 10], 4))