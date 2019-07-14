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
