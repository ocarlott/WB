class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        sSet = set(J) # O(N)
        for c in S: # O(M)
            if c in sSet:
                total += 1
        return total

# O(N + M) for time. O(N) for space.
