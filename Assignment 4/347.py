import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for key in counter.keys():
            if len(heap) < k:
                heapq.heappush(heap, (counter[key], key))
            else:
                heapq.heappushpop(heap, (counter[key], key))
        return list(map(lambda x: x[1], heap))
# O(NLogN) for time. O(M) for space.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return sorted(counter, key=counter.get, reverse=True)[:k]
# O(NLogN) for time. O(M) for space.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) # O(N)
        length = len(counter)
        keys = counter.keys()
        if length > k:
            while length > k: # O(sqrt(N) - K)
                for key in keys:
                    counter[key] -= 1
                    if counter[key] == 0:
                        length -= 1
        else:
            return counter.keys()
        result = []
        for key in keys: # O(M)
            if counter[key] > 0:
                result.append(key)
        return result

# O(N) for time. O(M) for space.
