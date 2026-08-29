# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        val = -1
        def inorder(root):
            nonlocal counter, val
            if root:
                inorder(root.left)
                counter += 1
                if counter == k:
                    val = root.val
                inorder(root.right)

        inorder(root)
        return val
