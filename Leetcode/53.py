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

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def getMax(nums, index):
            if index == 0:
                return (nums[0], nums[0])
            else:
                (localMax, globalMax) = getMax(nums, index - 1)
                localMax = max(localMax + nums[index], nums[index])
                globalMax = localMax if localMax > globalMax else globalMax
                return (localMax, globalMax)
        (localMax, globalMax) = getMax(nums, len(nums) - 1)
        return globalMax
# O(N) for time. O(1) for space.
