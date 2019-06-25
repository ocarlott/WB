class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)): # O(N)
            if (target - nums[i]) not in s:
                s[nums[i]] = i
            else:
                return [s[target - nums[i]], i]
# O(N) for time. O(N) for space.
