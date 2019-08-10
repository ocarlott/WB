from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.weight = {}
        
    def addEdge(self, u, v, weight):
        self.graph[u].append(v)
        self.weight[(u, v)] = weight
        
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = Graph()
        for pair in times:
            g.addEdge(pair[0], pair[1], pair[2])
        cost = [200] * N
        def dijsktra(g, cost, visited, start):
            cost[start - 1] = 0
            q = deque()
            q.append(start)
            while q:
                current = q.popleft()
                if current not in visited:
                    for n in g.graph[current]:
                        q.append(n)
                        if cost[n - 1] > cost[current - 1] + g.weight[(current, n)]:
                            cost[n - 1] = cost[current - 1] + g.weight[(current, n)]
                            if n in visited:
                                visited.remove(n)
                    visited.add(current)
        
        dijsktra(g, cost, set(), K)
        time = max(cost)
        return time if time != 200 else -1
# O(V + E) for time and space.
