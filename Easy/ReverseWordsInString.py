def reverse_words(s: str) -> str:
    s = s.split()
    s.reverse()
    return " ".join([i for i in s if i is not ""])


def reverse_words_v2(s: str) -> str:
    return " ".join(reversed(s.split()))


def reverse_words_v3(s: str) -> str:
    return " ".join(s.strip().split()[::-1])


if __name__ == '__main__':
    print(reverse_words("  hello world!  "))
