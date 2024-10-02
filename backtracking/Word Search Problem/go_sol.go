// https://leetcode.com/problems/word-search/
package main

import "fmt"

func backtrack(board [][]byte, i int, j int, index int, result *bool, word string) {

	if i < 0 || i >= len(board) || j < 0 || j >= len(board[0]) || index >= len(word) || board[i][j] != word[index] {
		return
	}

	if index == len(word)-1 {
		fmt.Println(index)
		*result = true
	}

	// temp change to prevent more than one visit in the same path
	temp := board[i][j]
	board[i][j] = '#'

	// movement in 4 directions
	backtrack(board, i+1, j, index+1, result, word)
	backtrack(board, i-1, j, index+1, result, word)
	backtrack(board, i, j+1, index+1, result, word)
	backtrack(board, i, j-1, index+1, result, word)

	board[i][j] = temp
}

func exist(board [][]byte, word string) bool {
	result := false

	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			if board[i][j] == word[0] {
				backtrack(board, i, j, 0, &result, word)
			}
		}
	}

	return result
}
