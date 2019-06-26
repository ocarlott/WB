class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        total = 0
        for i in range(32): # O(LogN)
            bitMask = 1 << i # O(1)
            if bitMask > x and bitMask > y:
                break
            if (bitMask & x) != (bitMask & y):
                total += 1
        return total
# O(LogN) for time. O(1) for space.
