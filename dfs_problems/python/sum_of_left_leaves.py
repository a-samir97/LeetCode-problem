from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(root):
            nonlocal result
            if root is None:
                return

            if root.left and root.left.left is None and root.left.right is None:
                result += root.left.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return result
