def check_record(s: str) -> bool:
    if len(s) < 2:
        return True

    if s.count("A") > 1:
        return False

    ans = 0 if s[0] != "L" else 1
    for i in s[1:]:
        if i == "L":
            ans += 1
            if ans > 2:
                return False
        else:
            ans = 0
    return True


def check_record_ver_2(s: str) -> bool:
    return not s.count("A") > 1 and not "LLL" in s


if __name__ == '__main__':
    print(check_record_ver_2("ALL"))
