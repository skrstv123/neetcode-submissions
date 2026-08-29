# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(ra, rb):
            if (ra and rb) and (ra.val == rb.val):
                return check(ra.right, rb.right) and check(ra.left, rb.left)
            return ra is None and rb is None
        
        def checksub(r, sr):
            same = check(r, sr)
            if same:
                return True
            ls = rs = False
            if r.left:
                ls = checksub(r.left, sr)
            if r.right:
                rs = checksub(r.right, sr)
            return ls or rs
        
        return checksub(root, subRoot)
            

