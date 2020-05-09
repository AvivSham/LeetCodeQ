from typing import List


def generate(numRows: int) -> List[List[int]]:
    if numRows == 0:
        return []

    if numRows == 1:
        return [[1]]

    ans = [[1]]
    for i in range(1, numRows):
        row = [1]
        for j in range(1, i+1):
            if j == i:
                row.append(1)
            else:
                row.append(ans[i - 1][j - 1] + ans[i - 1][j])
        ans.append(row)

    return ans


if __name__ == '__main__':
    print(generate(2))