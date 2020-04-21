from typing import List


def fizzBuzz(n: int) -> List[str]:
    if n == 0:
        return [0]

    ans = []
    for i in range(1, n + 1):

        if i % 15 == 0:
            ans.append("FizzBuzz")
        elif i % 3 == 0:
            ans.append("Fizz")
        elif i % 5 == 0:
            ans.append("Buzz")
        else:
            ans.append(str(i))
    return ans


if __name__ == '__main__':
    print(fizzBuzz(1000))