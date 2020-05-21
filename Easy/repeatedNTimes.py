from typing import List


def repeated_n_times(A: List[int]) -> int:
    h = [0 for _ in range(max(A) + 1)]
    for i in A:
        if h[i] == 0:
            h[i] += 1
        else:
            return i


def repeated_n_times_ver_2(A: List[int]) -> int:
    help_ = set()
    for i in A:
        if i not in help_:
            help_.add(i)
        else:
            return i


if __name__ == '__main__':
    print(repeated_n_times_ver_2([2,1,2,5,3,2]))
