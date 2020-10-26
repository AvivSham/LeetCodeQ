def multiply(num1: str, num2: str) -> str:
    """at first we will define a function (cvt_str_int) which will convert each given string to integer"""
    def cvt_str_int(num):
        new_num = 0
        order = len(num) - 1
        for i in num:
            new_num += (ord(i) - 48) * 10 ** order
            order -= 1
        return new_num

    return str(cvt_str_int(num1) * cvt_str_int(num2))


if __name__ == '__main__':
    print(multiply("9", "99"))
