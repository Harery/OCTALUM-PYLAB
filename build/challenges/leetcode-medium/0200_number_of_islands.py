"""
LeetCode 200: Number of Islands

Given a 2D binary grid of '1's (land) and '0's (water), count number of islands.
An island is surrounded by water and formed by connecting adjacent lands.

Example 1:
    Input: grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:
    Input: grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    Output: 3

Pattern: Island (DFS/BFS on Matrix)
Time: O(m * n)
Space: O(m * n) - recursion stack
"""

from __future__ import annotations


class Solution:
    def solve(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count


if __name__ == "__main__":
    solution = Solution()

    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    import copy

    test_cases = [
        (copy.deepcopy(grid1), 1),
        (copy.deepcopy(grid2), 3),
        ([["1"]], 1),
        ([["0"]], 0),
    ]

    for grid, expected in test_cases:
        result = solution.solve(grid)
        status = "✓" if result == expected else "✗"
        print(f"{status} Expected: {expected} | Got: {result}")
