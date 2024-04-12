# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

def solution(root):
    
    q = deque()
    q.append((root, (0, 0)))
    column_dict = defaultdict(dict)

    while len(q):
        node, (row, col) = q.popleft()
        if node:
            if row not in column_dict[col]:
                column_dict[col][row] = []

            column_dict[col][row].append(node.val)
            q.append((node.left, (row+1,col-1)))
            q.append((node.right, (row+1,col+1)))
            
    res = []
    for col in sorted(column_dict.keys()):
        res_col = []
        for row in sorted(column_dict[col].keys()):
            res_col.extend(sorted(column_dict[col][row]))
        res.append(res_col)
    return res


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        return solution(root)
        
