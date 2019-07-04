from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = Counter(s) # O(N)
        for c in t: # O(N)
            if counter[c] == 0:
                return c
            else:
                counter[c] -= 1
                
# O(N) for time and space.
