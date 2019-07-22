class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        codes = self.grayCode(n - 1)
        heading = 1 << (n - 1)
        oLength = len(codes)
        for i in range(oLength):
            codes.append(codes[oLength - 1 - i] + heading)
        return codes
# O(2^N) for time and space.

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        for i in range(n):
            result.extend([(2**i + result[-j]) for j in range(1, len(result) + 1)])
        return result

# O(2^N) for time and space.
