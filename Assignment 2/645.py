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
    
# O(N) for time and space
