class Solution:
    def titleToNumber(self, s: str) -> int:
        base = ord("A") - 1
        result = 0
        for c in s:
            result = result * 26 + ord(c) - base
        return result
# O(n) for time - n being the length of input. O(1) for space
