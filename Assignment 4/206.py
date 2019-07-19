# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        nex = cur.next
        cur.next = None
        while nex:
            prev = cur
            cur = nex
            nex = cur.next
            cur.next = prev
        return cur
# O(N) for time. O(1) for space
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        prev = head
        while cur.next: # O(N)
            prev = cur
            cur = cur.next
        prev.next = None
        cur.next = self.reverseList(head)
        return cur
    
# O(N^2) for time and space.
