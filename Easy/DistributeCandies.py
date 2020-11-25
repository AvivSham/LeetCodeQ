from typing import List


def distributeCandies(candyType: List[int]) -> int:
    u = set(candyType)
    max_ = len(candyType) // 2
    return len(u) if len(u) <= max_ else max_
