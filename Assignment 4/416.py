class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        total = 0
        maximum = 0
        for n in nums:
            total += n
            maximum = n if n > maximum else maximum
        if total % 2 != 0:
            return False
        half = total // 2
        if maximum > half:
            return False
        def solve(nums, index, target):
            if target == 0:
                return True
            if target < 0:
                return False
            for i in range(index, len(nums)):
                if solve(nums, i + 1, target - nums[i]):
                    return True
            return False
        return solve(nums, 0, half)
