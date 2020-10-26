def check_number_v1(num):
    """
    Runtime exceeded
    :param num: input number integer -> check if this is perfect number
    :return: bool True/False if the input is perfect number of not
    """
    if num <= 0:
        return False
    count = 1
    for i in range(2, num ** 2, 1):
        if num % i == 0:
            count += i + num / i
            if count > num:
                return False
            if count == num:
                return True
    return False


def check_number_v2(num):
    """
    Faster way
    :param num: input number integer -> check if this is perfect number
    :return: bool True/False if the input is perfect number of not
    """
    if num <= 1:
        return False

    div = list(filter(lambda x: num % x == 0, range(1, int(num**0.5)+1)))
    div = div + list(map(lambda x: int(num / x), div))[1:]
    return True if sum(div) == num else False


if __name__ == '__main__':
    print(check_number_v1(28))
    print(check_number_v2(1))
