def hamming_weight(n: int) -> int:
    return bin(n).replace("0b", "").count("1")


if __name__ == '__main__':
    print(hamming_weight(0o00000111))
