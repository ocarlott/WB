class Solution:
    def binaryGap(self, N: int) -> int:
        if N == 0:
            return 0
        count = 0
        maxCount = 0
        while N > 0:
            if N & 1 == 1:
                if count > maxCount:
                    maxCount = count
                count = 1
            else:
                if count > 0:
                    count += 1
            N = N >> 1 # Shift 1 bit a time, so total cost is O(LogN)
        return maxCount
# O(LogN) for time. O(1) for space
