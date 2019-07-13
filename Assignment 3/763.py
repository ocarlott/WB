from collections import Counter, defaultdict

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        counter = Counter(S) # O(M = nums of unique chars in S)
        cur = defaultdict(int)
        lastPart = -1
        result = []
        workingSet = set()
        for i, c in enumerate(S): # O(N)
            cur[c] += 1
            if cur[c] == counter[c]:
                if c in workingSet:
                    workingSet.remove(c)
                if len(workingSet) == 0:
                    result.append(i - lastPart)
                    lastPart = i
                    cur = defaultdict(int)
            else:
                workingSet.add(c)
        return result
# O(N) for time. O(M) for space.
