# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs -> Go through every level
        res = []

        def bfs(root, level):
            nonlocal res

            if root == None:
                return
            
            #append new level array
            if len(res) < level + 1:
                res.append([])

            #adding the current node to our list
            res[level].append(root.val)

            bfs(root.left, level+1)
            bfs(root.right, level+1)
        
        bfs(root, 0)
        return res