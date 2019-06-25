class Solution:
    def findComplement(self, num: int) -> int:
        mask = 0
        for i in range(33): # O(logn). Try to find correct mask
            mask += 2 ** i
            if num <= mask:
                break
        return ~num & mask
# O(logn) for time. O(1) for space
