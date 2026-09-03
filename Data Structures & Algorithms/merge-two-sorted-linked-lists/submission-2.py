# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()

        merged = []
        curr = list1
        curr2 = list2

        curr_list = head

        while curr or curr2:

            if not curr:
                curr_list.next = curr2
                curr2 = None
                
            elif not curr2:
                curr_list.next = curr
                curr = None
                
            else:
                if curr.val < curr2.val:
                    curr_list.next = curr
                    curr = curr.next
                else:
                    curr_list.next = curr2
                    curr2 = curr2.next
            
            curr_list = curr_list.next
        
        return head.next
            


