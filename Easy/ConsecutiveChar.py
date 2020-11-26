def max_power(s: str) -> int:
    max_ = 1
    curr = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            curr += 1
        else:
            if curr > max_:
                max_ = curr
            curr = 1
    return max(max_, curr)


if __name__ == '__main__':
    max_power("ccbccbb")