from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums) # O(N) for time and space
        missing = 0
        repeated = 0
        for i in range(1, len(nums) + 1): # O(N)
            if i not in counter:
                missing = i
            elif counter[i] == 2:
                repeated = i
        return [repeated, missing]
    
# O(N) for time and space.

# This solution has some math involved but saves space.
# The idea is to construct 2 equations so we can solve for a and b (repeated and missing)
# If we take the original array and subtract it with an array from 1 to n, we end up with x = a - b (Since there are 2 "a"s and no b)
# If we take an array with each element is a squared of a coresponding element in original array and subtract it with an array of 1^2 to n^2, we have y = a^2 - b^2
# Using 2 equations above, we can solve a = (y//x + x)/2 and b = (y//x - x)/2

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        x = y = 0
        for i in range(len(nums)):
            x += nums[i] - (i + 1) # Since element starts from 1
            y += nums[i] * nums[i] - (i + 1) * (i + 1)
        return [(y // x + x) // 2, (y // x - x) // 2]
    
# O(N) for time. O(1) for space.
