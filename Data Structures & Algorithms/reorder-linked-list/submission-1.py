# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Run through list and put in array
        nodes = []
        
        curr = head

        #put all nodes into array
        while curr != None:
            nodes.append(curr)
            curr = curr.next

        #set two pointers equal to head and tail of the array
        left = 0
        right = len(nodes) - 1
        while right > left:
            #interweave then nodes
            temp_node = nodes[left].next
            nodes[left].next = nodes[right]
            nodes[right].next = temp_node

            #move both pointers in by one
            left = left + 1
            right = right - 1

        
        nodes[left].next = None

       