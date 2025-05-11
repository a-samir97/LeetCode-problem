# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        """
        even levels -> increasing and odd numbers 
        odd levels -> decreasing and even numbers
        """
        if root.val % 2 == 0:
            return False
        
        queue = [root]
        level = 0
        while queue:
            # for each level
            n = len(queue)
            j = 0
            max_val = -1
            min_val = 10000000000000000
            while j < n:
                node = queue[0]
                queue = queue[1:]
                if level % 2 != 0:
                    if node.val >= min_val: return False
                    if node.val % 2 != 0: return False
                    min_val = node.val
                else:
                    if node.val <= max_val: return False
                    if node.val % 2 == 0: return False
                    max_val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                j += 1
            # increase level
            level += 1
        return True
