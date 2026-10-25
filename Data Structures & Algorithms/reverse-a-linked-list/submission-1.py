# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv = None
        curr = head
        if not curr:
            return head
        nx = curr.next
        while nx:
            curr.next = prv
            prv = curr
            curr = nx
            nx = curr.next
        head = curr
        curr.next = prv
        return head
        