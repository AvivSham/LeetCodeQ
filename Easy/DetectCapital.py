def detect_capital_use(word: str) -> bool:
    if len(word) == 0:
        return False

    if word.isupper():
        return True

    elif word[0].isupper() and word[1:].islower():
        return True

    elif word.islower():
        return True

    return False


if __name__ == '__main__':
    print(detect_capital_use("ASD"))
    print(detect_capital_use("AasdasdSD"))
    print(detect_capital_use("asdasd"))
