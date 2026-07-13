# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #equivalent 

        #run through each node of the tree somehow -> DFS
        #at each node check the value

        #assumes that the trees are equal
        equal = True

        #in: firstTree: p, secondTree: q
        #out: none
        def dfs(firstNode, secondNode):
            #modify the global var instead of making copy
            nonlocal equal

            #basecase: one after a tree node
            if firstNode == None and secondNode == None:
                return

            elif firstNode == None or secondNode == None:
                equal = False
                return

            if firstNode.val != secondNode.val:
                equal = False
                #done evaluating
                return
            
            dfs(firstNode.left, secondNode.left)
            dfs(firstNode.right, secondNode.right)
        
        dfs(p, q)
        return equal
        
