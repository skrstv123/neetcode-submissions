# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def godeep(r):
            if not r:
                return 0
            left = godeep(r.left)
            right = godeep(r.right)
            return max(left, right) + 1
        return godeep(root)
        