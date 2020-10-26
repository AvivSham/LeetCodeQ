import math


def climb_stairs(n: int) -> int:

    if n % 2:
        min_steps = n // 2 + 1
    else:
        min_steps = n // 2

    ans = 0

    for i in range(min_steps, n + 1):
        ans += math.factorial(i) / (math.factorial(2 * i - n) * math.factorial(n - i))

    return int(ans)


if __name__ == '__main__':
    print(climb_stairs(4))
