# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #fast and slow pointe method

        #set up fast and slow pointer
        slow = head
        fast = head

        
        #run while fast != None
        while fast != None and fast.next != None:
           
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

            

