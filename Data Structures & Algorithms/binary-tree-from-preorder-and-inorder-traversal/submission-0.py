# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pridx = 0
        inorderidx = {e:i for i,e in enumerate(inorder)}
        
        def arrtree(l, r):
            nonlocal pridx
            if l > r:
                return None
            pritem = preorder[pridx]
            ioidx = inorderidx[pritem]
            
            root = TreeNode(val=pritem)
            
            pridx += 1
            root.left = arrtree(l, ioidx-1)
            root.right = arrtree(ioidx+1, r)
            
            return root
        
        return arrtree(0, len(inorder)-1)

