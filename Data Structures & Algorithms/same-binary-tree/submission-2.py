# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


        
        p_deque = deque()
        q_deque = deque()

        p_deque.append(p)
        q_deque.append(q)

        while p_deque and q_deque:
            p_node = p_deque.pop()
            q_node = q_deque.pop()

            if p_node is None and q_node is None:
                continue

            if p_node is None or q_node is None:
                return False

            if p_node.val != q_node.val:
                return False

            p_deque.append(p_node.left)
            p_deque.append(p_node.right)
            q_deque.append(q_node.left)
            q_deque.append(q_node.right)
        
        return True


