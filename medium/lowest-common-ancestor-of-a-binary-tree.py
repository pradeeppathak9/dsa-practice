https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p, path_q = [], []
        def dfs(root, path):
            if not root: 
                return 
            path.append(root)

            if path[-1].val == p.val:
                nonlocal path_p
                path_p = path.copy()
            if path[-1].val == q.val:
                nonlocal path_q
                path_q = path.copy()

            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()
            return
            
        dfs(root, [])
        # print([i.val for i in path_p], [i.val for i in path_q])
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i].val != path_q[i].val:
                i -= 1
                break
        return path_p[i] 


            




        
        
