class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        i = 0
        for c in t:
            if c == s[i]:
                i += 1
                if i == len(s):
                    return True
        return i == len(s)
# O(N) for time. O(1) for space.
