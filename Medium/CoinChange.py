from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    dp = [0] + [amount+1]*amount

    for i in range(1, len(dp)):
        for coin in coins:
            if coin > i:
                continue
            else:
                dp[i] = min(dp[i-coin] + 1, dp[i])

    if dp[-1] == amount+1:
        return -1
    else:
        return dp[-1]


if __name__ == '__main__':
    print(coin_change([186, 419, 83, 408], 6249))
