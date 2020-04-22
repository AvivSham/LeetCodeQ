from typing import List

from collections import Counter

def commonChars(A) -> List[str]:
    """
    :type A: List[str]
    :rtype: List[str]
    """
    common: List[str] = [c for c in A[0]]
    c = Counter(A[0])
    ans = []
    for letter, counter in c.items():
        value = counter
        for word in A[1:]:
            count = word.count(letter)
            if count == 0:
                value = 0
                break
            if value > count:
                value = count
        ans += [letter] * value

    return ans


if __name__ == '__main__':
    print(commonChars(
["cool","lock","cook"]))