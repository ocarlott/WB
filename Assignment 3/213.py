class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def calc(nums, start, end):
            dp = (0, 0)
            for i in range(start, end + 1):
                withCur = dp[1] + nums[i]
                withoutCur = max(dp[0], dp[1])
                dp = (withCur, withoutCur)
            return max(dp[0], dp[1])
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            f = calc(nums, 0, len(nums) - 2)
            s = calc(nums, 1, len(nums) - 1)
            return max(f, s)

# O(N) for time. O(1) for space       

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def calc(nums, i, end):
            if i == end:
                return (nums[i], 0)
            value = calc(nums, i - 1, end)
            withCur = value[1] + nums[i]
            withoutCur = max(value[0], value[1])
            return (withCur, withoutCur)
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            f = calc(nums, len(nums) - 2, 0)
            s = calc(nums, len(nums) - 1, 1)
            return max(f[0], f[1], s[0], s[1])

# O(N) for time. O(1) for space     
