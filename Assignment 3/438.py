class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lengthP = len(p)
        p = sorted(p) # O(MLog(M)) for time. O(M) for space.
        lengthS = len(s)
        result = [] # O(N) for space
        if lengthS < lengthP:
            return result
        for i in range(lengthS - lengthP + 1): # O(N)
            sub = sorted(s[i:i+lengthP]) # O(MLog(M))
            if sub == p:
                result.append(i)
        return result

# O(NMLog(M)) for time. O(N + M) for space
