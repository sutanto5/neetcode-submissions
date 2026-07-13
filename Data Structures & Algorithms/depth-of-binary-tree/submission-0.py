# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #run preorder traversal -> root left right

        #recurison

        #base case: -> Leaf Node
        if root == None:
            return 0
        
        depth = 1

        left = root.left
        right = root.right

        leftDepth = self.maxDepth(left)
        rightDepth = self.maxDepth(right)

        if leftDepth > rightDepth:
            return depth + leftDepth
        else:
            return depth + rightDepth
        
