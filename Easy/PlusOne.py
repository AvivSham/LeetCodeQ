from typing import List


def plusOne(digits: List[int]) -> List[int]:
    """
    :param digits:  list of ints represent a number for example [1,2,3] -> 123
    :return: the represented input number plus one for example: [1,2,3] (123) -> [1,2,4] (124)
    """
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
                return digits


if __name__ == '__main__':
    print(plusOne([9]))