def remove_duplicates(S: str) -> str:
    r = S[0]
    for i in range(1, len(S)):
        if len(r) == 0:
            r += S[i]
        else:
            if r[-1] == S[i]:
                if len(r) == 1:
                    r = ''
                else:
                    r = r[:-1]
            else:
                r += S[i]

    return r
