# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solution(root, targetSum):
    ans = []
    def dfs(root, targetSum, path):
        if root == None: 
            return
        path.append(root.val)
        if root.left == None and root.right == None:
            # leaf node
            if targetSum == root.val:
                ans.append(path.copy())    
        dfs(root.left, targetSum - root.val, path)
        dfs(root.right, targetSum - root.val, path) 
        path.pop()

    dfs(root, targetSum, [])
    return ans


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return solution(root, targetSum)
        
