# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        node = head
        def rec(node):
            # base case of the recu method
            if node is None or node.next is None:
                return node
            
            # swap the node and node.next
            nxt = node.next
            node.next = rec(nxt.next)
            nxt.next = node
            # rec
            return nxt
        return rec(node)
                