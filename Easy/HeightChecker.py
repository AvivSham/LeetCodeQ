from typing import List


def height_checker(heights: List[int]) -> int:
    sort_heights = sorted(heights)
    return sum(list(map(lambda x, y: x != y, heights, sort_heights)))


if __name__ == '__main__':
    print(height_checker([1, 1, 4, 2, 1, 3]))
