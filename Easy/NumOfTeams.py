from itertools import combinations
from typing import List


def num_teams(rating: List[int]) -> int:
    ans = 0
    for com in combinations(rating, 3):
        if (com[0] < com[1] < com[2]) or (com[0] > com[1] > com[2]):
            ans += 1

    return ans


if __name__ == '__main__':
    rating = [2, 5, 3, 4, 1]
    print(num_teams(rating))