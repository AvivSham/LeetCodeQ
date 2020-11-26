from typing import List


def distribute_candies(candytype: List[int]) -> int:
    u = set(candytype)
    max_ = len(candytype) // 2
    return len(u) if len(u) <= max_ else max_
