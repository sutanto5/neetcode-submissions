# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #while not a leaf we want to go through each node and change its right and left 

        #pre order -> root left right
        if root == None:
            return

        
        curr = root
            

        temp = curr.left
        curr.left = curr.right
        curr.right = temp
        self.invertTree(curr.left)
        self.invertTree(curr.right)

        


        #root doesnt change in a binary tree
        return root
        