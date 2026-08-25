"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        # {orig_node : copy_node}
        hash_nodes = {}


        # iterate once create a copy of each node
        curr = head

        while curr != None:
            curr_copy = Node(curr.val)
            hash_nodes[curr] = curr_copy
            curr = curr.next



        # iterate twice and link each node
        curr = head

        while curr:
            if curr.next:
                hash_nodes[curr].next = hash_nodes[curr.next]
            else:
                hash_nodes[curr].next = None
            
            if curr.random:
                hash_nodes[curr].random = hash_nodes[curr.random]
            else:
                hash_nodes[curr].random = None

            curr = curr.next
        
        if head:
            return hash_nodes[head]
        else:
            return None

