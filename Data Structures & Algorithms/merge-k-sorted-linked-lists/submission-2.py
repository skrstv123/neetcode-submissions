# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # def merge2(a, b):
        #     c = d = ListNode()
        #     while a and b:
        #         if a.val < b.val:
        #             c.next = a
        #             a = a.next
        #         else:
        #             c.next = b
        #             b = b.next
        #         c = c.next
        #     c.next = a if a else b
        #     return d.next
        
        # # N.log(K)
        # while len(lists) > 1:
        #     m = []
        #     for i in range(0, len(lists), 2):
        #         a = lists[i]
        #         b = lists[i+1] if i+1 < len(lists) else None
        #         ml = merge2(a, b)
        #         m.append(ml)
        #     lists = m
        # return lists[0] if lists else None

        hp = []
        for i, head in enumerate(lists):
            if head:
                hq.heappush(hp, (head.val, i, head))
        
        ans = ListNode()
        anscp = ans

        while hp:
            top = hq.heappop(hp)
            _, idx, tn = top
            anscp.next = tn
            anscp = anscp.next
            if tn.next:
                hq.heappush(hp, (tn.next.val, idx, tn.next))

        return ans.next
