from typing import List


def kids_with_candies(candies: List[int], extraCandies: int) -> List[bool]:
    if len(candies) < 2:
        return True

    max_c = max(candies)
    return [(max_c - c) <= extraCandies for c in candies]


if __name__ == '__main__':
    print(kids_with_candies(candies=[2, 3, 5, 1, 3], extraCandies=3))
