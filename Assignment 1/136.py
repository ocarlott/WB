class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n # A number XOR with itself will be 0
        return result
# O(n) for time. O(1) for space
