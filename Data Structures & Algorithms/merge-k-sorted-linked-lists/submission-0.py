# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2(a, b):
            c = d = ListNode()
            while a and b:
                if a.val < b.val:
                    c.next = a
                    a = a.next
                else:
                    c.next = b
                    b = b.next
                c = c.next
            c.next = a if a else b
            return d.next
        
        while len(lists) > 1:
            m = []
            for i in range(0, len(lists), 2):
                a = lists[i]
                b = lists[i+1] if i+1 < len(lists) else None
                ml = merge2(a, b)
                m.append(ml)
            lists = m
        return lists[0] if lists else None