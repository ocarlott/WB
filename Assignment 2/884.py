from collections import Counter, defaultdict

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        aDict = defaultdict(int) # O(N)
        bDict = defaultdict(int) # O(M)
        result = set()
        A = A.split(" ") # O(N)
        for word in A: # O(N)
            aDict[word] = aDict[word] + 1
        B = B.split(" ") # O(M)
        for word in B: # O(M)
            bDict[word] = bDict[word] + 1
        for word in A: # O(N)
            if aDict[word] == 1 and word not in bDict:
                result.add(word)
        for word in B: # O(M)
            if bDict[word] == 1 and word not in aDict:
                result.add(word)
        return list(result)

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A = A.split(" ") # O(N)
        A.extend(B.split(" ")) # O(M)
        counter = Counter(A) # O(N + M)
        result = []
        for key, value in counter.items(): # O(N + M)
            if value == 1:
                result.append(key)
        return result

# O(N + M) for time and space
