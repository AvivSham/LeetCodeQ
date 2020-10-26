from typing import List


def prefixes_div_by_5(A: List[int]) -> List[bool]:
    ls = [str(A[0])]
    for i in range(1, len(A)):
        ls.append(ls[i - 1] + str(A[i]))
    return list(map(lambda x: int(x, 2) % 5 == 0, ls))


def prefixes_div_by_5_ver2(A: List[int]) -> List[bool]:
    pre = 0
    for i in range(len(A)):
        pre = pre << 1
        cur = pre + A[i]
        if cur % 5 == 0:
            A[i] = True
        else:
            A[i] = False
        pre = cur
    return A


if __name__ == '__main__':
    print(prefixes_div_by_5([0, 1, 1]))
    print(prefixes_div_by_5_ver2([0, 1, 1]))
