from typing import List


def final_prices(prices: List[int]) -> List[int]:
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] <= prices[i]:
                prices[i] = prices[i] - prices[j]
                break
    return prices


if __name__ == '__main__':
    p_list = [8, 4, 6, 2, 3]
    print(final_prices(p_list))
