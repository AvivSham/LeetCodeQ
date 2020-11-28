from typing import List


def maxProfit(prices: List[int]) -> int:

    buy_p = 0
    prof = 0

    for i in range(1, len(prices)):
        if prices[i] >= prices[i-1]:  # buy time
            if not buy_p:
                buy_p = prices[i-1]
            if i == len(prices) - 1:
                prof += prices[-1] - buy_p

        if (i <= len(prices)-2) and (prices[i] > prices[i+1]):
            if buy_p:
                prof += prices[i] - buy_p
                buy_p = 0
    return prof

def sol(prices: List[int]) -> int:

    maxp = 0

    # corner case
    if not prices or not prices[1:]: return maxp

    buy = None

    for i in range(1, len(prices)):

        if prices[i] >= prices[i - 1]:  # determine the buy time
            if buy is None:
                buy = prices[i - 1]
            if i == len(prices) - 1:  # sell when reach the end
                maxp = maxp + prices[i] - buy

        if i <= len(prices) - 2 and prices[i] > prices[i + 1]:  # determine the sell time
            if buy is not None:
                maxp = maxp + prices[i] - buy
                buy = None

    return maxp


if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit([1, 2, 3, 4, 5]))
