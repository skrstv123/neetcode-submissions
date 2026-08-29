# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sp = ep = head
        i = 0
        while i < n and ep:
            i += 1
            ep = ep.next

        if not ep:
            head = head.next
            return head
        
        while ep.next:
            ep = ep.next
            sp = sp.next
        
        sp.next = sp.next.next
        return head