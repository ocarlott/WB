class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        total = 0
        for i in range(32): # O(LogN)
            bitMask = 2 ** i # O(LogI)
            if bitMask > x and bitMask > y:
                break
            if (bitMask & x) != (bitMask & y):
                total += 1
        return total
# O(NLogN) for time. O(1) for space.
