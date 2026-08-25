# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        curr = head
        prev = head
        carry = 0


        while l1 != None or l2 != None:
            
            val1 = 0
            val2 = 0

            if l1:
                val1 = l1.val
            if l2:
                val2 = l2.val
            


            summation = carry + val1 + val2
            print(summation)

            if summation > 9:
                curr.val =  summation - 10
                print(curr.val)
                carry = 1
                temp = ListNode(0, None)

                curr.next = temp
                prev = curr
                curr = temp

            else:
                # update head pointer
                curr.val = summation
                carry = 0
                temp = ListNode(0, None)

                # iterate to next node
                curr.next = temp
                prev = curr
                curr = temp

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
            

        if curr.val == 0 and carry == 0:
            prev.next = None
        elif carry == 1:
            curr.val += 1

        return head
            