
def licenseKeyFormatting(S: str, K: int) -> str:

    # make sure all the characters are capital and remove "-"
    S = S.replace("-", "")
    if not S.isupper():
        S = S.upper()

    # in case of short string
    if len(S) < K:
        return S

    ans = ''
    if len(S) % K == 0:
        for i in range(0, len(S), K):
            ans += S[i:i + K]
            ans += "-"

    else:
        ans += S[:int(len(S) % K)]
        ans += "-"
        for i in range(int(len(S) % K), len(S), K):
            ans += S[i:i + K]
            ans += "-"
    # return ans but the last character which is "-"
    return ans[:-1]


def licenseKeyFormatting_ver2(S: str, K: int) -> str:
    S = S.replace("-", "")
    if not S.isupper():
        S = S.upper()

    # in case of short string
    if len(S) < K:
        return S


if __name__ == '__main__':
    print(licenseKeyFormatting("2-5-3-J", 3))
