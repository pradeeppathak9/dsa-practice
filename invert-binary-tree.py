# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def dfs(root):
#     if not root:
#         return
#     temp = root.left
#     root.left = root.right
#     root.right = temp
#     dfs(root.left)
#     dfs(root.right)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right = root.right, root.left 
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


    
        
