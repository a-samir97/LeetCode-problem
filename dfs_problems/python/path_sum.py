from typing import Optional
# https://leetcode.com/problems/path-sum/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = -1000000000000

    def traverse_tree(self,root, targetSum, result):
        if root is None:
            return

        result += root.val
        if root and root.left is None and root.right is None:
            if result == targetSum: self.result = targetSum

        if root.left: self.traverse_tree(root.left, targetSum, result)
        if root.right: self.traverse_tree(root.right, targetSum, result)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        self.traverse_tree(root, targetSum, 0)

        return True if self.result == targetSum else False
