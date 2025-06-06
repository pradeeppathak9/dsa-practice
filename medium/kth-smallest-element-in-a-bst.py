# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def solution(root, k):
    inorder = []
    def dfs(root):
        if root == None:
            return
        dfs(root.left)
        inorder.append(root.val)
        dfs(root.right)
    dfs(root)
    return inorder[k-1]


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return solution(root, k)
        
