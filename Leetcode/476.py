class Solution:
    def findComplement(self, num: int) -> int:
        mask = 0
        for i in range(32): # O(logn). Try to find correct mask
            mask += 2 ** i # O(logi). Log(1) + Log(2) + .. + Log(N) < NLogN. Can precompute this to make this an O(LogN) algo.
            if num <= mask:
                break
        return ~num & mask
# O(nlogn) for time. O(1) for space
