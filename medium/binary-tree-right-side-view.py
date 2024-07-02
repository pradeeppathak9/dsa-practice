# https://leetcode.com/problems/binary-tree-right-side-view/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution with DFS
def solution(root):
    ans = []
    max_level = 0
    def dfs(root, level):
        nonlocal max_level
        if root == None:
            return
        if level == max_level: 
            ans.append(root.val)
            max_level += 1

        dfs(root.right, level+1)
        dfs(root.left, level+1)
    dfs(root, 0)
    return ans

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return solution(root)



# Solution using BFS 

from collections import deque, defaultdict
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque()
        q.append((root, 0))
        while len(q):
            node, level = q.popleft()
            if node:
                if level >= len(result):
                    result.append(node.val)
                q.append((node.right, level+1))
                q.append((node.left, level+1))            
        return result
