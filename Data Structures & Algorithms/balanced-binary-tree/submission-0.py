# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

   
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #O(n) -> need to go through each node and calculate its height
        balanced = True

        #return a pair of value -> bool and height of tree
        def dfs(root):
            nonlocal balanced

            #base case:
            if not root: 
                return 0
            
            #run dfs on left and right
            left, right = dfs(root.left), dfs(root.right)

            #check if it is balanced
            if abs(left - right) > 1:
                balanced = False
            
            return 1 + max(left, right)

        dfs(root)
        return balanced
            
        