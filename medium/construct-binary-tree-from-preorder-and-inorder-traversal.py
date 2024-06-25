# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        index = inorder.index(preorder[0])
        return TreeNode(
            preorder[0], 
            left = self.buildTree(preorder[1: 1+index], inorder[:index]),
            right = self.buildTree(preorder[1+index: ], inorder[index+1:]),
        )
        
