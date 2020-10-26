from typing import List
from itertools import combinations


def check_straight_line(coordinates: List[List[int]]) -> bool:
    def find_slope(points):
        try:
            return (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
        except:
            return 1e5

    return True if len(set(map(find_slope, list(combinations(coordinates, 2))))) == 1 else False


if __name__ == '__main__':
    print(check_straight_line([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
