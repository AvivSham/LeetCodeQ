def int_to_roman(num: int) -> str:
    d = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    s, q, n, m = '', num, 1, 5

    while (q):
        q, resi = divmod(q, 10)

        if 0 < resi < 4:
            s = d[n] * resi + s

        elif resi == 4:
            s = d[n] + d[m] + s

        elif resi == 5:
            s = d[m] + s

        elif 5 < resi < 9:
            s = d[m] + d[n] * (resi - 5) + s

        elif resi == 9:
            s = d[n] + d[10 * n] + s

        m *= 10
        n *= 10

    return s


if __name__ == '__main__':
    print(int_to_roman(60))