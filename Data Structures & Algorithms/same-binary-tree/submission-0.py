# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(ra, rb):
            if (ra and rb) and (ra.val == rb.val):
                return check(ra.right, rb.right) and check(ra.left, rb.left)
            return ra is None and rb is None
        
        return check(p, q)
