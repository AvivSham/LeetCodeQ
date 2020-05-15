from typing import List


def k_weakest_rows(mat: List[List[int]], k: int) -> List[int]:
    s = [[sum(row), i] for i, row in enumerate(mat)]
    return [i[1] for i in sorted(s)][:k]


if __name__ == '__main__':
    print(k_weakest_rows(mat=
                         [[1, 1, 0, 0, 0],
                          [1, 1, 1, 1, 0],
                          [1, 0, 0, 0, 0],
                          [1, 1, 0, 0, 0],
                          [1, 1, 1, 1, 1]],
                         k=3))
