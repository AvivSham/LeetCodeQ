from typing import List


def islandPerimeter(grid: List[List[int]]) -> int:
    M, N, p = len(grid), len(grid[0]), 0
    for m in range(M):
        for n in range(N):
            if grid[m][n] == 1:
                # check for upper edge and left neighbor
                if m == 0 or not grid[m - 1][n]:
                    p += 1
                if n == 0 or not grid[m][n - 1]:
                    p += 1
                if n == N - 1 or not grid[m][n + 1]:
                    p += 1
                if m == M - 1 or not grid[m + 1][n]:
                    p += 1
    return p


if __name__ == '__main__':
    print(islandPerimeter([[0,1,0,0],
                           [1,1,1,0],
                           [0,1,0,0],
                           [1,1,0,0]]))