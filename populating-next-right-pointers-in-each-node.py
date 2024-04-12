# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque, defaultdict
def solution(root):
    res = defaultdict(list)
    q = deque()
    q.append((root, 0))
    while len(q):
        node, level = q.popleft()
        if node:
            res[level].append(node)
            q.append((node.left, level+1))
            q.append((node.right, level+1))
    
    for k in res.keys():
        for i in range(len(res[k]) - 1):
            res[k][i].next = res[k][i+1]
        res[k][-1].next = None
    return root

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        return solution(root)
        
