# https://leetcode.com/problems/binary-tree-level-order-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque, defaultdict
def solution(root):
    res = defaultdict(list)
    q = deque()
    q.append((root, 0))
    while len(q):
        node, level = q.popleft()
        if node:
            res[level].append(node.val)
            q.append((node.left, level+1))
            q.append((node.right, level+1))
    
    result = []
    for k in sorted(res.keys()):
        result.append(res[k])
    return result

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return solution(root)
        
