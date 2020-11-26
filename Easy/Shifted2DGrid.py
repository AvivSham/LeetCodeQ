from typing import List

"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.
"""


def shift_grid(grid: List[List[int]], k: int) -> List[List[int]]:
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            new_col = (col + k) % len(grid[0])
            new_row = (row + ((col + k) // len(grid[0]))) % len(grid)
            new_grid[new_row][new_col] = grid[row][col]

    return new_grid


if __name__ == '__main__':
    shift_grid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1)
