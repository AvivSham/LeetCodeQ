from typing import List


def selfDividingNumbers(left: int, right: int) -> List[int]:
    ans = []
    for i in range(left, right + 1):
        num_str = str(i)

        if len(num_str) == 1:
            ans.append(i)

        elif "0" not in num_str:
            count = 0
            for ind in range(len(num_str)):
                if i % int(num_str[ind]) != 0:
                    break
                else:
                    count += 1

            if count == len(num_str):
                ans.append(i)

    return ans


if __name__ == '__main__':
    print(selfDividingNumbers(1, 22))