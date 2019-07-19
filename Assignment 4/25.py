# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseKNodes(head, k):
    curPtr = head
    nexPtr = head.next
    prevPtr = None
    curPtr.next = prevPtr
    n = 1
    while nexPtr and n < k:
        n += 1
        prevPtr = curPtr
        curPtr = nexPtr
        nexPtr = curPtr.next
        curPtr.next = prevPtr
    return (curPtr, head, nexPtr, n)

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        if not head:
            return head
        (begin, end, nexPtr, n) = reverseKNodes(head, k)
        if n < k:
            (rBegin, rEnd, rNexPtr, m) = reverseKNodes(begin, k)
            return rBegin
        end.next = self.reverseKGroup(nexPtr, k)
        return begin
    
# O(N) for time. O(n/k) for space.
