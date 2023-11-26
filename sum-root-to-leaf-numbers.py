# https://leetcode.com/problems/sum-root-to-leaf-numbers/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def solution(root):
    ans = []
    def dfs(root, path):
        if root == None: 
            return
        if root.left == None and root.right == None:
            # leaf node
            s = 0
            for v in path:
                s = s*10 + v
            s = s*10 + root.val
            ans.append(s)
            return

        dfs(root.left, path + [ root.val ])
        dfs(root.right, path + [ root.val ]) 
        return ans
    dfs(root, [])
    return sum(ans)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return solution(root)
        
