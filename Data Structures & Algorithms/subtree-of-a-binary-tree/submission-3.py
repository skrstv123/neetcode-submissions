# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # powers = [31 ** i for i in range(1000)]
        # powers.reverse()

        # power_idx = lambda s, i: len(s) - i - 1

        # def serialize(root):
        #     if not root:
        #         return '.'
        #     return f'{root.val}({serialize(root.left)}{serialize(root.right)})'
        
        # roots = serialize(root)
        # subroots = serialize(subRoot)

        # if len(roots) < len(subroots):
        #     return False

        # hashroot = [ord(roots[i]) * powers[power_idx(roots, i)] for i in range(len(roots))]
        # hashsubroot = sum(ord(subroots[i]) * powers[power_idx(roots, i)] for i in range(len(subroots)))

        # for i in range(1, len(hashroot)):
        #     hashroot[i] += hashroot[i-1]
        
        # for i in range(len(roots) - len(subroots)):
        #     ei = i + len(subroots) - 1
        #     hashs = hashroot[ei]
        #     if i > 0:
        #         hashs -= hashroot[i-1]
        #     if hashs == hashsubroot:
        #         return True
        
        # return False

        MOD = 10**9 + 7  # Large prime to minimize collisions
        BASE = 911382629   # Another large prime (can be adjusted)
        max_length = 5000  # Sufficiently large to cover serialized trees
        
        # Precompute powers of BASE modulo MOD
        powers = [1] * max_length
        for i in range(1, max_length):
            powers[i] = (powers[i-1] * BASE) % MOD

        def serialize(node):
            if not node:
                return ''
            # Include val, left, and right in a way that avoids ambiguity
            return f"({node.val},{serialize(node.left)},{serialize(node.right)})"
        
        # Serialize both trees
        root_str = serialize(root)
        sub_str = serialize(subRoot)
        
        len_root = len(root_str)
        len_sub = len(sub_str)
        
        if len_root < len_sub:
            return False
        
        # Compute hash of subRoot's serialization
        sub_hash = 0
        for i in range(len_sub):
            sub_hash = (sub_hash + ord(sub_str[i]) * powers[len_sub - 1 - i]) % MOD
        
        # Compute rolling hash for root's serialization
        root_hash = 0
        # Initialize the first window (first len_sub chars of root_str)
        for i in range(len_sub):
            root_hash = (root_hash + ord(root_str[i]) * powers[len_sub - 1 - i]) % MOD
        
        # Early check for the first window
        if root_hash == sub_hash and root_str[:len_sub] == sub_str:
            return True
        
        # Slide the window and update the rolling hash
        for i in range(len_sub, len_root):
            # Remove the leftmost character's contribution
            root_hash = (root_hash - ord(root_str[i - len_sub]) * powers[len_sub - 1]) % MOD
            # Shift the hash left (multiply by BASE)
            root_hash = (root_hash * BASE) % MOD
            # Add the new character's contribution
            root_hash = (root_hash + ord(root_str[i])) % MOD
            
            # Check if the current window matches sub_str
            start = i - len_sub + 1
            if root_hash == sub_hash and root_str[start:i+1] == sub_str:
                return True
        
        return False
