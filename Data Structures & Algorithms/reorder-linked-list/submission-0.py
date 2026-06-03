# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse 2nd half
        sec = slow.next
        prv = slow.next = None
        while sec:
            temp = sec.next
            sec.next = prv
            prv = sec
            sec = temp

        #merge two halfs
        first , second = head, prv
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        
        