# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

class Solution:

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        # solution via dfs 
        ans = []
        def dfs(root, level):
            if not root:
                return
            if level == len(ans):
                ans.append(root.val)
            else:
                ans[level] = max(ans[level], root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)
        return ans
            


        q = deque()
        q.append((root, 0))
        res = {}
        max_level = -1
        while len(q):
            node, level = q.popleft()
            if node:
                res[level] = max(res[level], node.val) if level in res else node.val
                max_level = max(max_level, level)
                q.append((node.left, level+1))
                q.append((node.right, level+1))
        return [ res[i] for i in range(max_level + 1) ]

        
