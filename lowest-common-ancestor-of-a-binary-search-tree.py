# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(root, el, path):
    if root is None: return False
    path.append(root)
    if root.val == el: return True
    if dfs(root.left, el, path): return True
    if dfs(root.right, el, path):return True
    path.pop()
    return False

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1, path2 = [], [] 
        dfs(root, p.val, path1)
        dfs(root, q.val, path2)
        # print([el.val for el in path1])
        # print([el.val for el in path2])    
        i = 0
        while i < len(path1) and i < len(path2) and path1[i].val == path2[i].val:
            i+=1
            continue
        return path1[i-1]
        
    
        
