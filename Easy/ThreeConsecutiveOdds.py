from typing import List


def three_consecutive_odds(arr: List[int]) -> bool:
    stack = []

    for num in arr:
        if len(stack) == 3:
            stack.pop(0)
        stack.append(num % 2 == 1)

        if all(stack) and len(stack) == 3:
            return True

    return False
