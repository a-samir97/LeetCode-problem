func dfs(visited []bool, isConnected [][]int, city int) {
	stack := []int{city}
	visited[city] = true
	for len(stack) != 0 {
		c := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for i, j := range isConnected[c] {
			if i == c {
				continue
			}
			if j == 1 && visited[i] == false {
				stack = append(stack, i)
				visited[i] = true
			}

		}
	}
}

func findCircleNum(isConnected [][]int) int {
	result := 0
	visited := []bool{}

	for i := 0; i < len(isConnected); i++ {
		visited = append(visited, false)
	}

	for i := 0; i < len(isConnected); i++ {
		if visited[i] == false {
			dfs(visited, isConnected, i)
			result += 1
			fmt.Println(visited, i)
		}
	}
	return result
}