class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
       
        def checkEqual(root, subRoot):
            if not root and not subRoot:
                return True
            
            if not root or not subRoot:
                return False
            
            if root.val == subRoot.val:
                return (
                    checkEqual(root.right, subRoot.right)
                    and checkEqual(root.left, subRoot.left)
                )
            
            return False

        if not subRoot:
            return True
        
        if not root:
            return False

        if root.val == subRoot.val and checkEqual(root, subRoot):
            return True
        
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )