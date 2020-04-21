def add_strings(num1: str, num2: str) -> str:
    def cvt_to_num(num):
        numeric = 0
        order = len(num) - 1
        for i in num:
            numeric += (ord(i) - 48) * 10 ** order
            order -= 1
        return numeric

    return str(cvt_to_num(num1) + cvt_to_num(num2))


if __name__ == '__main__':
    add_strings("23423", "234234")