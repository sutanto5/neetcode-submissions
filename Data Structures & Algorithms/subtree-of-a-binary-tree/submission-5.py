# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #goal is to find subRoot within root

        #dfs
        def dfs(root):
            
            #base case: hit a leaf
            if root == None:
                return False

            #if subroot found then check for equivalency
            if root.val == subRoot.val:
                #slight in
                if equivalent(root, subRoot):
                    return True
            
            return dfs(root.left) or dfs(root.right)
        


        def equivalent(first, second):
            
            

            #if first = None, and second = None
            if first == None and second == None:
                return True

            #tree structure is not the same
            elif first == None or second == None:
                return False

            
            if first.val != second.val:
                return False
            
            #ineffeciency because
            return equivalent(first.left, second.left) and equivalent(first.right, second.right)


        return dfs(root)
        
