/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type RootLevel struct {
	node  *TreeNode
	level int
}

func maxLevelSum(root *TreeNode) int {
	level, counterSum := 1, 0
	maxVal, maxLevel := root.Val, 1

	queue := []RootLevel{{root, maxLevel}}

	for len(queue) != 0 {
		curr_node := queue[0]
		queue = queue[1:]

		if level == curr_node.level {
			counterSum += curr_node.node.Val
		} else {
			// check max
			if maxVal < counterSum {
				maxLevel = level
				maxVal = counterSum
			}
			counterSum = curr_node.node.Val
			level = curr_node.level
		}
		if len(queue) == 0 {
			if maxVal < counterSum {
				maxVal = counterSum
				maxLevel = level
			}
		}
		if curr_node.node.Right != nil {
			queue = append(queue, RootLevel{curr_node.node.Right, curr_node.level + 1})
		}
		if curr_node.node.Left != nil {
			queue = append(queue, RootLevel{curr_node.node.Left, curr_node.level + 1})
		}
	}
	return maxLevel
}