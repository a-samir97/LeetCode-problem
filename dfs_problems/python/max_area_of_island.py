from typing import List
# https://leetcode.com/problems/max-area-of-island/


class Solution:
    def valid(self, i, j, grid):
        return (i >= 0 and i < len(grid)) and (j >= 0 and j < len(grid[i]))

    def dfs(self, i, j, grid):
        if grid[i][j] == 0: return 0
        grid[i][j] = 0

        ret = 1
        # 4 directions 
        if self.valid(i, j+1, grid): ret += self.dfs(i, j+1, grid)
        if self.valid(i, j-1, grid): ret += self.dfs(i, j-1, grid)
        if self.valid(i+1, j, grid): ret += self.dfs(i+1, j, grid)
        if self.valid(i-1, j, grid): ret += self.dfs(i-1, j, grid)
        return ret

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                    temp = self.dfs(i, j, grid)
                    ans  = temp if temp > ans else ans
        return ans
