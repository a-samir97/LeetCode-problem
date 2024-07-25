from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        left = head

        # right pointers walking n steps 
        for i in range(0, n):
            right = right.next

        if right is None:
            return head.next

        # walking till the end for both right and left
        while right and right.next is not None:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return head
        
