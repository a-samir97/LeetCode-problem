class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = {}
        def helper(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i > m or j > n:
                return 0

            if i == m and j == n:
                return 1
            
            right = helper(i + 1, j) # right
            down = helper(i, j + 1) # down
            memo[(i,j)] = right + down
            return memo[(i,j)]
        return helper(1, 1)