# https://leetcode.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def solution(root):
#     res = []
#     def dfs(root):
#         if root == None:
#             return
#         dfs(root.left)
#         res.append(root.val)
#         dfs(root.right)
#     dfs(root)
#     for i in range(1, len(res)):
#         if res[i] <= res[i-1]:
#             return False
#     return True

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         return solution(root)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)
        

