class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lastIndex = len(s) - 1
        if lastIndex >= 1:
            for i in range(lastIndex // 2 + 1):
                s[i], s[lastIndex - i] = s[lastIndex - i], s[i]
# O(n) for time - n being string length. O(1) for space
