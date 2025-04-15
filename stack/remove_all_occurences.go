package main

func removeOccurrences(s string, part string) string {
	var stack []byte

	for i := 0; i < len(s); i++ {
		stack = append(stack, s[i])
		// check substring of the stack
		if len(stack) >= len(part) && string(stack[len(stack)-len(part):]) == part {
			stack = stack[:len(stack)-len(part)]
		}
	}

	return string(stack)
}
