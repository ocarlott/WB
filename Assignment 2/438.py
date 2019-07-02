from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lengthP = len(p) # O(M)
        pCounter = Counter(p) # O(M)
        lengthS = len(s) # O(N)
        result = [] # O(N) for space
        if lengthS < lengthP:
            return result
        sCounter = Counter(s[:lengthP]) # O(M) for space
        if sCounter == pCounter:
            result.append(0)
        for i in range(lengthP, lengthS):
            currentCount = sCounter[s[i - lengthP]]
            if currentCount == 1: # Sliding window technique. Delete the one before and add the one after M length
                del(sCounter[s[i - lengthP]])
            else:
                sCounter[s[i - lengthP]] = currentCount - 1
            sCounter[s[i]] += 1
            if sCounter == pCounter: # O(M)
                result.append(i - lengthP + 1)
        return result

# O(NM) for time. O(N + M) for space
