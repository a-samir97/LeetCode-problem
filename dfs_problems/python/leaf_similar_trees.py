from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, result):
            if root is None: return 

            if root.left is None and root.right is None:
                result.append(root.val)

            dfs(root.left, result)
            dfs(root.right, result)

        result1, result2 = [], []
        dfs(root1, result1)
        dfs(root2, result2)
        return result1 == result2
