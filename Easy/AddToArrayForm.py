from typing import List


def add_to_array_form(A: List[int], K: int) -> List[int]:
    return list(str(int("".join(list(map(str, A)))) + K))


if __name__ == '__main__':
    print(add_to_array_form([9, 9, 9, 9], 1))
