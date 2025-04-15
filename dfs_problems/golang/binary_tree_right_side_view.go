/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func dfs(root *TreeNode, result []int, level int, states map[int]bool) []int {

	if root == nil {
		return result
	}

	if root.Right != nil && root.Left != nil {
		if _, ok := states[level]; !ok {
			states[level] = true
			result = append(result, root.Right.Val)
		}
		result = dfs(root.Right, result, level+1, states)
		result = dfs(root.Left, result, level+1, states)
	} else if root.Right != nil {
		if _, ok := states[level]; !ok {
			states[level] = true
			result = append(result, root.Right.Val)
		}
		result = dfs(root.Right, result, level+1, states)
	} else if root.Left != nil {
		if _, ok := states[level]; !ok {
			states[level] = true
			result = append(result, root.Left.Val)
		}
		result = dfs(root.Left, result, level+1, states)
	}
	return result
}
func rightSideView(root *TreeNode) []int {

	var result []int
	if root == nil {
		return result
	}
	result = append(result, root.Val)
	return dfs(root, result, 0, make(map[int]bool))
}