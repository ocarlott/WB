class Solution:
    def findComplement(self, num: int) -> int:
        mask = 0
        for i in range(32): # O(LogN). Try to find correct mask
            mask += 1 << i # O(1)
            if num <= mask:
                break
        return ~num & mask # O(LogN)
# O(LogN) for time. O(1) for space
