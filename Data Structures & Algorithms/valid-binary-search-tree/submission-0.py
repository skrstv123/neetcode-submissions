# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def vbst(root, minv = -float('inf'), maxv = float('inf')):
            if not root:
                return True
            if root.val <= minv or root.val >= maxv:
                return False
            return vbst(root.left, minv, root.val) and vbst(root.right, root.val, maxv)

        return vbst(root)