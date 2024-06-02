from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []
        number = 0

        def dfs(root):
            nonlocal number
            if root is None: return 

            result.append(root.val)

            if root.left is None and root.right is None:
                number += int("".join(str(x) for x in result))

            dfs(root.left)
            dfs(root.right)
            result.pop()

        dfs(root)
        return number
