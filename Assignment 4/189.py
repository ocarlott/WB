class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        for i in range(k):
            temp = nums.pop()
            nums.insert(0, temp)
# O(NK) for time. O(1) for space

from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        queu = deque(nums[::-1])
        for i in range(k):
            queu.append(queu.popleft())
        for i in range(-1, -len(nums) - 1, -1):
            nums[i] = queu.popleft()

# O(N) for time and space
