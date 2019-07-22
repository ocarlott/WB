class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [nums.copy()]
        while True:
            i = len(nums) - 1
            while i > 0:
                if nums[i] > nums[i - 1]:
                    break
                i -= 1
            if i == 0:
                break
            j = len(nums) - 1
            while nums[j] < nums[i - 1]:
                j -= 1
            nums[j], nums[i - 1] = nums[i - 1], nums[j]
            j = len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            result.append(nums.copy())
            
        return result
# O(n!) for time and space.
