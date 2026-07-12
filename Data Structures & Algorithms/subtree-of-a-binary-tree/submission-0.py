# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialise(node):
            if not node:
                return ["#"]
            return  [str(node.val)]  +serialise(node.left)+serialise(node.right)
        r1="".join(serialise(root))
        r2="".join(serialise(subRoot))
        print(r1,r2)
        return r2 in r1