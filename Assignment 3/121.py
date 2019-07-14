class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        def getMax(prices, index):
            if index == len(prices) - 1:
                return (prices[index], 0)
            else:
                (maxSell, maxProfit) = getMax(prices, index + 1)
                maxSell = max(prices[index], maxSell)
                maxProfit = max(maxProfit, maxSell - prices[index])
                return (maxSell, maxProfit)
            
        (maxSell, maxProfit) = getMax(prices, 0)
        return maxProfit
# O(N) for time. O(1) for space.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        globalBest = 0
        localBest = 0
        minBuy = prices[0]
        for n in range(1, len(prices)):
            localBest = max(localBest, prices[n] - minBuy)
            minBuy = min(prices[n], minBuy)
            globalBest = max(localBest, globalBest)
        return max(globalBest, 0)
# O(N) for time. O(1) for space.
