# https://leetcode.com/problems/binary-tree-level-order-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque, defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        res = []
        while q:
            level_res = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level_res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level_res:
                res.append(level_res)
        return res
        
