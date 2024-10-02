# https://leetcode.com/problems/word-search/
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False

        def backtrack(board, i, j, index):
            nonlocal result
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or index >= len(word) or board[i][j] != word[index]:
                return

            if index == len(word) - 1:
                result = True

            temp = board[i][j]
            board[i][j] = "@"

            # movement in 4 directions
            backtrack(board, i-1, j, index + 1)
            backtrack(board, i+1, j, index + 1)
            backtrack(board, i, j+1, index + 1)
            backtrack(board, i, j-1, index + 1)

            board[i][j] = temp

        backtrack(board, 0, 0, 0)

        return result
