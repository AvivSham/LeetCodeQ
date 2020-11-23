def freq_alphabets(s: str) -> str:
    r = ''
    l = len(s)
    i = 0
    while i < l:
        if i < l - 2 and s[i + 2] == '#':
            r += chr(96 + int(s[i:i + 2]))
            i += 3
        else:
            r += chr(96 + int(s[i]))
            i += 1
    return r
