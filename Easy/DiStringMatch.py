from typing import List


def di_string_match(S: str) -> List[int]:
    s = len(S)
    n = 0
    ans = []
    for i in S:
        if i == "I":
            ans.append(n)
            n += 1
        else:
            ans.append(s)
            s -= 1
    ans.append(n) if S[-1] == "I" else ans.append(s)
    return ans


if __name__ == '__main__':
    print(di_string_match("D"))