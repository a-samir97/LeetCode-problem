func canVisitAllRooms(rooms [][]int) bool {
	states := make(map[int]bool)
	for i, _ := range rooms {
		states[i] = false
	}
	states[0] = true
	stack := []int{0}
	// set the first room with it's keys

	for len(stack) != 0 {
		node := stack[0]
		stack = stack[1:]
		for _, k := range rooms[node] {
			if states[k] == false {
				states[k] = true
				stack = append(stack, k)
			}
		}
	}

	for i := 0; i < len(rooms); i++ {
		if states[i] == false {
			return false
		}
	}
	return true
}