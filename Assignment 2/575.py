class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        kinds = set()
        for candy in candies: # O(N)
            kinds.add(candy)
        return min(len(kinds), len(candies) // 2)

# O(N) for time and space.
