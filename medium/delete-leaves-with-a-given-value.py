# https://leetcode.com/problems/delete-leaves-with-a-given-value/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if node.left and dfs(node.left):
                node.left = None
            if node.right and dfs(node.right):
                node.right = None
            if node.val == target and node.left is None and node.right is None:
                return True
            return False
        return None if dfs(root) else root
        
        









        
