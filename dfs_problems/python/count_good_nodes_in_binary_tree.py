# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = []
        good_count = 0

        def dfs(root):
            nonlocal good_count
            if root is None: return

            result.append(root.val)
            good_count += 1 if max(result) == result[-1] else 0
            if root.left: dfs(root.left)
            if root.right: dfs(root.right)
            result.pop()
        dfs(root)

        return good_count
