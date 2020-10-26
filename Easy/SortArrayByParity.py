from typing import List


def sortArrayByParity(A) -> List[int]:
    odd: List = []
    even: List = []
    for num in A:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even + odd


if __name__ == '__main__':
    print(sortArrayByParity([3, 1, 2, 4]))
