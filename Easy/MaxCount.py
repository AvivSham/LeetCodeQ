from typing import List


def max_count(m: int, n: int, ops: List[List[int]]) -> int:
    return min([i[0] for i in ops]) * min([i[1] for i in ops]) if ops else m * n


if __name__ == '__main__':
    print(max_count(3, 3, [[2, 2], [3, 3]]))
