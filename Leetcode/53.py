class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        globalMax = localMax = nums[0]
        for i in range(1, len(nums)):
            localMax = max(localMax + nums[i], nums[i])
            if localMax > globalMax:
                globalMax = localMax
        return globalMax
# O(N) for time. O(1) for space.
