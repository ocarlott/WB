# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        ptrO = partO = head
        ptrE = partE = head.next
        head = head.next.next
        counter = 1
        while head:
            if counter % 2 == 1:
                ptrO.next = head
                ptrO = head
            else:
                ptrE.next = head
                ptrE = head
            head = head.next
            counter += 1
        ptrE.next = None
        ptrO.next = partE
        return partO
# O(N) for time. O(1) for space.
