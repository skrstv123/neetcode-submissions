# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if root:
                l = root.left
                r = root.right
                root.left = r
                root.right = l
                if l:
                    invert(l)
                if r:
                    invert(r)
        invert(root)
        return root;
        