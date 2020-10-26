from typing import List

from collections import Counter


def top_k_frequent(words: List[str], k: int) -> List[str]:
    words = sorted(words)
    freq = Counter(words)
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [i[0] for i in freq[:k]]


if __name__ == '__main__':
    print(top_k_frequent(["i", "love", "leetcode", "i", "love", "coding"], k=2))
