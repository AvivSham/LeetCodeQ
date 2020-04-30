from collections import Counter


def find_the_difference(s: str, t: str) -> str:
    if set(s) != set(t):
        return (set(t) - set(s)).pop()

    else:
        s = Counter(s)
        t = Counter(t)
        for i, j in s.items():
            if j != t[i]:
                return i


if __name__ == '__main__':
    print(find_the_difference("aada", "aasda"))