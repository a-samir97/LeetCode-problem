from typing import List
# https://leetcode.com/problems/number-of-islands/


class Solution:
    def valid(self, i, n, j, m):
        return (i >= 0 and i < n) and (j < m and j >= 0)

    def dfs(self, i, j, grid):
        if grid[i][j] == '0': return

        # Mark as visited 
        grid[i][j] = '0'
        # move in 4 directions
        # right => i, j+1
        # left => i, j-1
        # up => i+1, j
        # down => i-1, j
        if self.valid(i,len(grid), j+1, len(grid[i])) and grid[i][j+1] == '1': self.dfs(i, j+1, grid)
        if self.valid(i, len(grid), j-1, len(grid[i])) and grid[i][j-1] == '1': self.dfs(i, j-1, grid)
        if self.valid(i+1, len(grid), j, len(grid[i])) and grid[i+1][j] == '1': self.dfs(i+1, j, grid)
        if self.valid(i-1, len(grid), j, len(grid[i])) and grid[i-1][j] == '1': self.dfs(i-1, j, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    ans += 1

        return ans