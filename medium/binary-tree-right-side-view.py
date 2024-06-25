# https://leetcode.com/problems/binary-tree-right-side-view/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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
