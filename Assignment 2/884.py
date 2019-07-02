class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        aDict = {} # O(N)
        bDict = {} # O(M)
        result = set()
        A = A.split(" ") # O(N)
        for word in A: # O(N)
            aDict[word] = aDict.get(word, 0) + 1
        B = B.split(" ") # O(M)
        for word in B: # O(M)
            bDict[word] = bDict.get(word, 0) + 1
        for word in A: # O(N)
            if aDict[word] == 1 and word not in bDict:
                result.add(word)
        for word in B: # O(M)
            if bDict[word] == 1 and word not in aDict:
                result.add(word)
        return list(result)

# O(N + M) for time and space
