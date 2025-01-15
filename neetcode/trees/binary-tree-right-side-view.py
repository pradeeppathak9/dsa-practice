# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = {}
        q = deque()
        q.append((root, 0))
        max_level = 0
        while len(q):
            node, level = q.popleft()
            if node:
                result[level] = node.val
                max_level = max(max_level, level)
                q.append((node.left, level+1))
                q.append((node.right, level+1))          

        return list(result.values())

        
