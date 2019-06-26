class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lengths = len(s)
        lengtht = len(t)
        if lengths == 0 and lengtht == 0:
            return True
        if lengths != lengtht:
            return False
        mp = {}
        for c in s: # O(N)
            mp[c] = mp.get(c, 0) + 1
        for c in t: # O(N)
            count = mp.get(c, 0)
            if count == 0:
                return False
            else:
                mp[c] = count - 1
        return True
# O(N) for time. O(N) for space
