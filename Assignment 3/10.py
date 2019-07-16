class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] for i in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0].append(dp[0][j - 2])
            else:
                dp[0].append(False)
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

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = { (0, 0): True }
        
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                cache[(0, j)] = cache[(0, j - 2)]
            else:
                cache[(0, j)] = False
        
        for i in range(1, len(s) + 1):
            cache[(i, 0)] = False
                                      
        def testMatch(s, p, i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            value = False
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                value = testMatch(s, p, i - 1, j - 1)
            elif p[j - 1] == '*':
                zeroCharBefore = testMatch(s, p, i, j - 2)
                oneOrMoreCharBefore = testMatch(s, p, i - 1, j) if s[i - 1] == p[j - 2] or p[j - 2] == '.' else False
                value = zeroCharBefore or oneOrMoreCharBefore
            else:
                value = False
            cache[(i, j)] = value
            return value
        return testMatch(s, p, len(s), len(p))

# O(NM) for time and space.
