def reverse_str(s: str, k: int) -> str:
    if len(s) < k:
        return s[::-1]

    if k <= len(s) < 2 * k:
        return s[:k][::-1] + s[k:]

    ans = ""
    for i in range(0, len(s), 2 * k):
        ans += s[i:i + k][::-1] + s[i + k:i + 2 * k]
    return ans


if __name__ == '__main__':
    print(reverse_str("abcdefg", 2))
