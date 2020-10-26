def roman_to_int(s: str) -> int:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    i = 0
    ans = 0
    sub = 0
    while i < len(s)-1:
        if roman[s[i]] < roman[s[i + 1]]:
            sub += roman[s[i]]
        else:
            ans += roman[s[i]] - sub
            sub = 0
        i += 1

    return ans - sub + roman[s[-1]]


def roman_to_int_v2(s: str) -> int:
    if not s:
        return 0
    DictRI = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    res = 0
    L = len(s)
    for i in range(L - 1):
        if DictRI[s[i]] < DictRI[s[i + 1]]:
            res -= DictRI[s[i]]
        else:
            res += DictRI[s[i]]
    res += DictRI[s[L - 1]]
    return res


if __name__ == '__main__':
    print(roman_to_int("VMMM"))
