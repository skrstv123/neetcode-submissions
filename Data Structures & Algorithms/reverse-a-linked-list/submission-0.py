# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ph = None
        h = head
        hn = head.next if head else None

        while h:
            h.next = ph
            ph = h

            h = hn
            if h:
                hn = h.next

        return ph if ph else h