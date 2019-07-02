class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        count = {}
        for candy in candies: # O(N)
            count[candy] = count.get(candy, 0) + 1
        return min(len(count.keys()), len(candies) // 2)

# O(N) for time and space.
