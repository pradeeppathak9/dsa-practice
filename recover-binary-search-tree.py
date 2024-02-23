# https://leetcode.com/problems/recover-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solution(root):
    inorder = []
    def dfs(root):
        if root == None:
            return
        dfs(root.left)
        inorder.append(root)
        dfs(root.right)
    dfs(root)
  
    i = j = None
    for i in range(len(inorder)-1):
        if inorder[i].val > inorder[i+1].val:
            break
    
    for j in range(len(inorder)-1, 0, -1):
        if inorder[j].val < inorder[j-1].val:
            break
          
    val = inorder[i].val
    inorder[i].val = inorder[j].val
    inorder[j].val = val
    return 


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        solution(root)
        
