from typing import List
# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/


class Solution:
    def __init__(self):
        self.visited = set()

    def valid(self, i, n, j, m):
        # check if i, j inside grid
        return (i >= 0 and i < n) and (j >= 0 and j < m) and (i,j) not in self.visited
       
    def dfs(self, i, n, j, m, grid):
        if not self.valid(i, n, j, m) or grid[i][j] == 0:
            return 0

        self.visited.add((i, j))
        result = grid[i][j]
        
        result += self.dfs(i, n, j+1, m, grid) + self.dfs(i, n, j-1, m, grid) + self.dfs(i+1, n, j, m, grid) + self.dfs(i-1, n, j, m, grid)
        return result

    def findMaxFish(self, grid: List[List[int]]) -> int:
        max_number = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] != 0 and (i,j) not in self.visited:
                    max_number = max(max_number, self.dfs(i, len(grid), j, len(grid[i]), grid))
        return max_number
