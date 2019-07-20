# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for ls in lists:
            while ls:
                heapq.heappush(heap, ls.val)
                ls = ls.next
        if len(heap) == 0:
            return None
        head = ListNode(heapq.heappop(heap))
        tail = head
        while len(heap) > 0:
            tail.next = ListNode(heapq.heappop(heap))
            tail = tail.next
        return head
# O(NMLog(NM)) for time. O(NM) for space.
