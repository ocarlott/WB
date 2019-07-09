class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        mid = (left + right) // 2
        while True:
            if nums[mid] == target:
                return mid
            if left == mid or right == mid:
                return -1
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            mid = (left + right) // 2
# O(Log(N)) for time. O(1) for space.
