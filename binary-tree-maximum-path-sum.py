# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        def dfs(root):
            if root is None:
                return 0
            max_left = max(dfs(root.left), 0)
            max_right = max(dfs(root.right), 0)
            # ans with split, the path goes from current node
            nonlocal ans
            ans = max(ans, root.val + max_right + max_left)
            # return ans without split
            return root.val + max(max_left, max_right)
        dfs(root)
        return ans


            
        
