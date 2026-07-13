# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #create a new list
        X = []

        #have two pointers pointing at next unmerged node
        one_pointer = list1
        two_pointer = list2

        prev = None
        #run while both are not null
        while(one_pointer != None and two_pointer != None):
            if one_pointer.val < two_pointer.val:
                X.append(one_pointer)
                
                if prev == None:
                    prev = one_pointer
                else:
                    prev.next = one_pointer
                    prev = one_pointer

                one_pointer = one_pointer.next

            else:
                X.append(two_pointer)

                if prev == None:
                    prev = two_pointer

                else:
                    prev.next = two_pointer
                    prev = two_pointer

                two_pointer = two_pointer.next
        if(prev == None):
            X.append(one_pointer or two_pointer)
        else:
            prev.next = one_pointer or two_pointer
            
        return X[0]