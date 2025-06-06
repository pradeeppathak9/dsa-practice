# https://leetcode.com/problems/count-good-nodes-in-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root, max_val):
            if root is None:
                return
            if root.val >= max_val:
                nonlocal ans
                ans += 1
            
            dfs(root.left, max(max_val, root.val))
            dfs(root.right, max(max_val, root.val))

        dfs(root, root.val)
        return ans
        


