class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(max(nums[i] + sums[i - 1], nums[i]))
        result = nums[0]
        for n in sums:
            if n > result:
                result = n
        return result
# O(N) for time and space.
