def removeOuterParentheses(S):
    """
    :type S: str
    :rtype: str
    """
    r = 0
    l = 0
    start = 0
    ss = ""
    for i in range(len(S)):
        if S[i] == "(":
            r += 1
        else:
            l += 1

        if l == r:
            ss += S[start + 1:i]
            start = i + 1
            r = 0
            l = 0
    return ss

if __name__ == '__main__':
    print(removeOuterParentheses("(()())(())(()(()))"))