# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def inorderTraversal(self, node: Optional[TreeNode]) :
        if not node:
            return []
        
        
        return self.inorderTraversal(node.left) + [node.val] + self.inorderTraversal(node.right)