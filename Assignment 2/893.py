class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        wordSet = set() # O(N) for space
        for word in A: # { word: (even_set(), odd_set()) } # O(N)
            wEven = word[::2] # O(M) for time and space
            wOdd = word[1::2]  # O(M)
            wordSet.add((frozenset(wEven), frozenset(wOdd))) # Convert list to frozenset takes O(M) and add takes O(1).
        return len(wordSet)
    
# O(NM) for time. O(N + M) for space.
