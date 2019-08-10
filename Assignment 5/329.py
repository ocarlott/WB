from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n, m = len(matrix), len(matrix[0])
        g = Graph()
        for r in range(n):
            for c in range(m):
                node = r * m + c
                if r != 0 and matrix[r - 1][c] > matrix[r][c]:
                    g.addEdge(node, node - m)
                if r != n - 1 and matrix[r + 1][c] > matrix[r][c]:
                    g.addEdge(node, node + m)
                if c != 0 and matrix[r][c - 1] > matrix[r][c]:
                    g.addEdge(node, node - 1)
                if c != m - 1 and matrix[r][c + 1] > matrix[r][c]:
                    g.addEdge(node, node + 1)
        dp = {}
        longestPath = 0
        def dfs(g, dp, node):
            if node in dp:
                return dp[node]
            pathLen = 1
            for c in g.graph[node]:
                pathLen = max(pathLen, 1 + dfs(g, dp, c))
            dp[node] = pathLen
            return pathLen
        
        for r in range(n):
            for c in range(m):
                node = r * m + c
                longestPath = max(longestPath, dfs(g, dp, node))
        return longestPath
            
# O(NM) for time and space.
