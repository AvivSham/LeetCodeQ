def reverse_words(s: str) -> str:
    if len(s) < 2:
        return s[::-1]

    return " ".join(list(map(lambda x: x[::-1], s.split())))


def reverse_words_ver2(s: str) -> str:
    s = s.split(' ')
    l = []
    for i in s:
        l.append(i[::-1])
    return ' '.join(l)


if __name__ == '__main__':
    print(reverse_words_ver2("aviv bla bla"))
