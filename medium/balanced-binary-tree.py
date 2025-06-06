# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def depth(node):
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            
            nonlocal is_balanced
            if abs(left - right) > 1:
                is_balanced = False
            return 1 + max(left, right)

        depth(root)
        return is_balanced

        
