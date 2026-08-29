# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def printlist(head):
            l = "[ "
            while head:
                l+=f"{head.val}, "
                head = head.next
            l += "]"
            print(l)

        def reverse(hp):
            ph = None
            h = hp
            nh = h.next if (h and h.next) else None 

            while h:
                h.next = ph
                ph = h
                h = nh
                if h:
                    nh = h.next
            return ph

        def findmid(head):
            s = f = head
            while f and f.next:
                s = s.next
                f = f.next.next
            return s
        
        mid = findmid(head)

        secondhead = reverse(mid)
        
        cfh = head

        while secondhead.next:

            fn = cfh.next
            sn = secondhead.next

            cfh.next = secondhead
            secondhead.next = fn

            cfh = fn
            secondhead = sn
        # return head








        