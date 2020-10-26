from typing import List


def k_closest(points: List[List[int]], K: int) -> List[List[int]]:
    def distance(point1: List[int], point2: List[int]):
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

    return sorted(points, key=lambda x: distance(x, [0, 0]))[:K]


if __name__ == '__main__':
    print(k_closest(points=[[1, 3], [-2, 2]], K=1))
