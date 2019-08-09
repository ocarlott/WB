from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.edges = set()
        
    def addEdge(self, u, v):
        if (u, v) not in self.edges:
            self.edges.add((u, v))
            self.edges.add((v, u))
            self.graph[u].append(v)

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        g = Graph()
        def dfs(row, col, visited, grid, g):
            if grid[row][col] == 0 or (row, col) in visited:
                return
            n, m = len(grid), len(grid[0])
            visited.add((row, col))
            if row != n - 1 and grid[row + 1][col] == 1:
                g.addEdge(row * m + col, (row + 1) * m + col)
                dfs(row + 1, col, visited, grid, g)
            if row != 0 and grid[row - 1][col] == 1:
                g.addEdge(row * m + col, (row - 1) * m + col)
                dfs(row - 1, col, visited, grid, g)
            if col != 0 and grid[row][col - 1] == 1:
                g.addEdge(row * m + col, row * m + col - 1)
                dfs(row, col - 1, visited, grid, g)
            if col != m - 1 and grid[row][col + 1] == 1:
                g.addEdge(row * m + col, row * m + col + 1)
                dfs(row, col + 1, visited, grid, g)

        n, m = len(grid), len(grid[0])
        visited = set()
        for i in range(n):
            for j in range(m):
                dfs(i, j, visited, grid, g)
        return len(visited) * 4 - len(g.edges)

# O(NM) for time. O(K) for space
        
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 4
                if j != m - 1:
                    if grid[i][j] == 1 and grid[i][j + 1] == 1:
                        count -= 2
                if i != 0:
                    if grid[i][j] == 1 and grid[i - 1][j] == 1:
                        count -= 2
        return count

# O(NM) for time. O(1) for space
