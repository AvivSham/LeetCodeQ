from typing import List
from collections import Counter


def uncommon_from_sentences(A: str, B: str) -> List[str]:
    A = A.split(" ")
    B = B.split(" ")

    ls1 = [i for i in A if i not in B and A.count(i) == 1]
    ls2 = [i for i in B if i not in A and B.count(i) == 1]
    return ls1+ls2


def uncommon_from_sentences_v2(A: str, B: str) -> List[str]:
    return [i for i, j in Counter(A.split(" ") + B.split(" ")).items() if j == 1]


def uncommon_from_sentences_v3(A: str, B: str) -> List[str]:
    ans = []
    shared_ls = A.split(" ") + B.split(" ")
    for i in shared_ls:
        if shared_ls.count(i) == 1:
            ans.append(i)

    return ans


if __name__ == '__main__':
    print(uncommon_from_sentences_v3("apple apple", "banana"))