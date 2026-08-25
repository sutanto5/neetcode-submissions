# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        front = head
        back = head
        arrStack = []

        while back.next:
            arrStack.append(back)
            back = back.next

        arrStack.append(back)
        
        seen = set()

        while front not in seen:
            back = arrStack.pop()
            
            if back == front:
                front.next = None
                break

            seen.add(back)

            temp = front.next
            front.next = back

            if temp in seen:
                back.next = None
                break

            back.next = temp
            front = temp
        