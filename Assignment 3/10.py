class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] for i in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0].append(dp[0][j - 2])
            else:
                dp[0].append(False)
                
        if len(p) > 1 and p[1] == "*":
            dp[0][2] = True
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i].append(dp[i - 1][j - 1])
                elif p[j - 1] == '*':
                    dp[i].append(dp[i][j - 2] or (dp[i - 1][j] if s[i - 1] == p[j - 2] or p[j - 2] == '.' else False))
                else:
                    dp[i].append(False)
        return dp[-1][-1]
# O(NM) for time and space.
