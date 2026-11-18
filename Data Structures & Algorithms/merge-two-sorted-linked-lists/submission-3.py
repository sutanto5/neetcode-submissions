# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        list3 = None

        if not list1:
            return list2
        
        if not list2:
            return list1
        
        if list1.val < list2.val:
            list3 = list1
            list1 = list1.next
        
        else:
            list3 = list2
            list2 = list2.next

        head = list3

        while list1 != None or list2 != None:

            # if list1 == None
            if list1 == None:
                list3.next = list2
                break

            # if list 2 == None
            elif list2 == None:
                list3.next = list1
                break

            # if neither
            else:
                if list1.val <= list2.val:
                    list3.next = list1
                    list1 = list1.next
                    list3 = list3.next
                else:
                    list3.next = list2
                    list2 = list2.next
                    list3 = list3.next
        return head

            