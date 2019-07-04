from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        # Need to count characters to sort. # O(N)
        # Sort characters by frequency # At least O(NLog(N)).
        # Construct a string with the sorted charaters set O(N)
        counterDict = Counter(s)
        sortedArr = []
        for key, value in counterDict.items(): # O(N^2 for 2 loops)
            current = (key, value)
            for i in range(len(sortedArr)):
                if current[1] > sortedArr[i][1]:
                    current, sortedArr[i] = sortedArr[i], current
            sortedArr.append(current)
        for i in range(len(sortedArr)): # O(N)
            sortedArr[i] = sortedArr[i][0] * sortedArr[i][1]
        return "".join(sortedArr)

# O(N^2) for time. O(N) for space.

class Solution:
    def frequencySort(self, s: str) -> str:
        # Need to count characters to sort. # O(N)
        # Sort characters by frequency # At least O(NLog(N)).
        # Construct a string with the sorted charaters set O(N)
        counterDict = Counter(s) # O(N)
        heap = []
        result = []
        for char, count in counterDict.items(): # O(NLog(N))
            heapq.heappush(heap, (count, char))
        for i in range(len(heap)): # O(N)
            tup = heapq.heappop(heap)
            result.append(tup[0] * tup[1])
        return "".join(result[::-1]) # O(N)

# O(NLog(N)) for time. O(N) for space.
