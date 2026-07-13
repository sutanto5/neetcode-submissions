# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #all values are unique
        #p and q are children of x in the same tree that are not the root

        #breadth first search x2
            # get the ancestors including p

            #get the ancestor including q
       
        #in: root of the tree, its target 
        #out: array -> stack of ancestor nodes
        def bfs(root, target):
            anc = []
            if root == None:
                return anc

            if root.val != target.val:
                anc.append(root)

                left =  bfs(root.left, target)
                right = bfs(root.right, target)

                #check for targt
                if target in left:
                    anc = anc + left
                if target in right:
                    anc = anc + right

                return anc

            else:
                anc.append(target)
                return anc

        p_anc = []
        p_anc = bfs(root, p)

        q_anc = []
        q_anc = bfs(root, q)

        

       

        q_vals = {node.val for node in q_anc}

        for i in range(len(p_anc) - 1, -1, -1):
            if p_anc[i].val in q_vals:
                return p_anc[i]
        

        #no common ancestor
        return root
        
        