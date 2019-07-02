class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        wordSet = set() # O(N) for space
        for word in A: # { word: (even_set(), odd_set()) } # O(N)
            wEven = word[::2] # O(M) for time and space
            wOdd = word[1::2]  # O(M)
            wordSet.add((''.join(sorted(wEven)), "".join(sorted(wOdd)))) # sorted takes O(MLog(M)), join takes O(M) and add takes O(1). These 3 operations work sequentially. Therefore, the dominant term is O(MLog(M))
        return len(wordSet)
    
# O(NMLog(M)) for time. O(N + M) for space.
