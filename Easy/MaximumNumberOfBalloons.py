from collections import Counter


def maxNumberOfBalloons(text: str) -> int:
    s = "balloon"
    arr = []
    if len(text) < len(s):
        return 0

    for char, count in Counter(s).items():
        if char not in text:
            return 0

        num = text.count(char) // count
        if not num:
            return 0

        arr.append(num)

    return min(arr)


if __name__ == '__main__':
    print(maxNumberOfBalloons("balloonballoo"))
