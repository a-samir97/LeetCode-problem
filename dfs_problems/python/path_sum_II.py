from typing import List, Optional
# https://leetcode.com/problems/path-sum-ii/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        temp = []
        result = []

        def traverse_tree(root, temp):
            if root is None:
                return
            temp.append(root.val)

            if root.left is None and root.right is None:
                if sum(temp) == targetSum:
                    # unexpected behavior, need to get copy of temp list 
                    result.append(temp.copy())
            traverse_tree(root.left, temp)
            traverse_tree(root.right, temp)
            temp.pop()

        traverse_tree(root, temp)
        return result
