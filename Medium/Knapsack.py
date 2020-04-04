def knapsack(max_weight, weights, values, n):
    cache = [[0 for _ in range(max_weight+1)] for _ in range(n+1)]
    # i iterates over values
    for i in range(n + 1):
        # j iterates over different max weight values
        for j in range(max_weight + 1):
            if i == 0 or j == 0:
                cache[i][j] = 0
            elif j >= weights[i-1]:
                cache[i][j] = max(cache[i-1][j - weights[i - 1]] + values[i - 1], cache[i - 1][j])
            else:
                cache[i][j] = cache[i-1][j]
    return cache[i][j]


if __name__ == '__main__':
    val = [50, 100, 150, 200]
    wt = [8, 16, 32, 40]
    W = 64
    n = len(val)
    print(knapsack(W, wt, val, n))