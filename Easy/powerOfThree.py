import math


def isPowerOfThree(n: int) -> bool:
    if n <= 0:
        return False
    return 3 ** round(math.log(n, 3)) == n


if __name__ == '__main__':
    print(isPowerOfThree(243))