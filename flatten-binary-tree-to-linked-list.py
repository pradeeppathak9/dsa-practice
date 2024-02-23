# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
        
def solution(root):
    preorder = []
    def dfs(root):
        if root == None:
            return
        preorder.append(root)
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    
    # print("res", [k.val for k in preorder])
    for i, node in enumerate(preorder):
        node.left = None
        node.right = None if i == len(preorder)-1 else preorder[i+1]

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        solution(root)

        


    
