from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None: return 0, True
            right, right_balance = dfs(root.right)
            left, left_balance = dfs(root.left)
            is_balanced = right_balance and left_balance and abs(left-right) <= 1
            return (1 + max(left, right), is_balanced)

        return dfs(root)[1]
