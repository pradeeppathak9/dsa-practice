# https://leetcode.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []
        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)
        dfs(root)
            
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i-1]:
                return False

        return True
        
        
