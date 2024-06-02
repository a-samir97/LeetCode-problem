from typing import List


class Solution:

    def valid_coords(self, i, n, j, m):
        return (i >= 0 and i < n) and (j >= 0 and j < m)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()

        def visit_o_border(i, j, board):
            if board[i][j] == 'X' or (i, j) in visited:
                return

            visited.add((i, j))

            # visit all O and make them visited so we can not change them 
            if self.valid_coords(i+1, len(board), j, len(board[0])): visit_o_border(i+1, j, board)
            if self.valid_coords(i-1, len(board), j, len(board[0])): visit_o_border(i-1, j, board)
            if self.valid_coords(i, len(board), j+1, len(board[0])): visit_o_border(i, j+1, board)
            if self.valid_coords(i, len(board), j-1, len(board[0])): visit_o_border(i, j-1, board)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if i == 0 or j == 0 or i == len(board) -1 or j == len(board[i]) -1:
                    if board[i][j] == 'O': visit_o_border(i, j, board)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
