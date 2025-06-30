# https://leetcode.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            
            # Right subtree must be greater
            if not dfs(node.right, val, upper):
                return False
            # Left subtree must be less
            if not dfs(node.left, lower, val):
                return False
            return True
        return dfs(root)
        
        
        
