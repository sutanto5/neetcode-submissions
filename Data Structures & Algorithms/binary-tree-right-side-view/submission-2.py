# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        currHeights = set()
        
        def rhs_traverse(root, currHeight):
            nonlocal res
            nonlocal currHeights

            if not root:
                return
            
            if currHeight not in currHeights:
                res.append(root.val)
                currHeights.add(currHeight)

            # rhs
            rhs_traverse(root.right, currHeight+1)
            # lhs
            rhs_traverse(root.left, currHeight+1)
            
        rhs_traverse(root, 0)

        return res


            
            
