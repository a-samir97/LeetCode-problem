# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # edge case if there is not root
        if root is None:
            return []
        
        queue = [(root, 0)]
        result = [root.val]
        s = set()

        while queue:
            node, level = queue.pop()
            if node.right:
                if level not in s:
                    result.append(node.right.val)
                    s.add(level)
            if node.left:
                if level not in s:
                    result.append(node.left.val)
                    s.add(level)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result