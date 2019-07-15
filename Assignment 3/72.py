class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for j in range(l1 + 1)] for i in range(l2 + 1)]
        for i in range(1, l1 + 1):
            dp[0][i] = i
        for i in range(1, l2 + 1):
            dp[i][0] = i
        for row in range(1, l2 + 1):
            for col in range(1, l1 + 1):
                nForSub = 0 if word1[col - 1] == word2[row - 1] else 1
                dp[row][col] = min(dp[row - 1][col - 1] + nForSub, dp[row][col - 1] + 1, dp[row - 1][col] + 1)
        return dp[l2][l1]
# O(NM) for time and space.
