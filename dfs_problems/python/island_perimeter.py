from typing import List


class Solution:
    def validate(self, i, n, j, m):
        return (i >= 0 and i < n) and (j >= 0 and j < m)

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        visited = set()

        def dfs(i, j, grid):
            nonlocal result
            nonlocal visited
            if grid[i][j] == 0 or (i, j) in visited:
                return

            result += 4
            visited.add((i, j))

            if self.validate(i+1, len(grid), j, len(grid[0])) and grid[i+1][j] == 1: 
                result -= 1
                dfs(i+1, j, grid)
            if self.validate(i-1, len(grid), j, len(grid[0])) and grid[i-1][j] == 1:
                result -= 1
                dfs(i-1, j, grid)
            if self.validate(i, len(grid), j+1, len(grid[0])) and grid[i][j+1] == 1:
                result -= 1
                dfs(i, j+1, grid)
            if self.validate(i, len(grid), j-1, len(grid[0])) and grid[i][j-1] == 1:
                result -= 1
                dfs(i, j-1, grid)

        dfs(0, 0, grid)

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    dfs(i, j, grid)
        return result
