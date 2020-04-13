

def to_goat_latin(S: str) -> str:
    v = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    S = S.split(" ")
    for i, w in enumerate(S):
        if w[0] in v:
            S[i] = w + "ma" + "a" * (i + 1)
        else:
            S[i] = w[1:] + w[0] + "ma" + "a" * (i + 1)
    return " ".join(S)


if __name__ == '__main__':
    print(print(to_goat_latin("I speak Goat Latin")))