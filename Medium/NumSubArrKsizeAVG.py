from typing import List


def num_of_sub_arrays(arr:List[int], k:int, threshold:int):
    ans, sum_ = 0, 0
    stack = []

    for n in arr:
        stack.append(n)

        if len(stack) > k:
            sum_ -= stack.pop(0)
        sum_ += n

        if len(stack) == k and sum_ / k >= threshold:
            ans += 1

    return ans


if __name__ == '__main__':
    print(num_of_sub_arrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))
