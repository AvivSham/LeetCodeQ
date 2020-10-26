def tribonacci(n: int) -> int:
    if n < 2:
        return n
    if n == 2:
        return 1

    fibi = [-1 for _ in range(n + 1)]
    fibi[0] = 0
    fibi[1] = 1
    fibi[2] = 1

    for i in range(3, len(fibi)):
        fibi[i] = fibi[i - 3] + fibi[i - 2] + fibi[i - 1]

    return fibi[-1]


if __name__ == '__main__':
    print(tribonacci(10))
