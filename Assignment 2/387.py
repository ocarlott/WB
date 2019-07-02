from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {} # O(N) for space
        length = len(s)
        fIndex = length
        for i in range(length): # O(N)
            (index, count) = freq.get(s[i], (i, 0))
            if count == 0:
                freq[s[i]] = (i, 1)
            else:
                freq[s[i]] = (index, count + 1)
        for value in freq.values(): # O(N)
            if value[1] == 1 and fIndex > value[0]:
                fIndex = value[0]
        result = fIndex if fIndex < length else -1
        return result
        
# O(N) for time and space.
