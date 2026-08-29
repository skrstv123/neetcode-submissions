# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as dq

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = dq([root])
        ans = []
        while q:
            qvals = q
            q = dq([])
            cans = [r.val for r in filter(lambda x: x is not None, qvals)]
            if cans:
                ans.append(cans)
            for node in qvals:
                if node:
                    q.append(node.left)
                    q.append(node.right)
        return ans



