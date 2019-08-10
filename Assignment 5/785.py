from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nu = 2
        s = { 1: set(), 2: set() }
        processed = {}
        g = Graph()
        for i in range(len(graph)):
            for n in graph[i]:
                g.addEdge(i, n)
        for i in range(len(graph)):
            if i not in processed:
                processed[i] = 1
                queue = deque()
                queue.append(i)
                s[1].add(i)
                while queue:
                    current = queue.popleft()
                    nex = processed[current] % nu + 1
                    for c in g.graph[current]:
                        if c in processed:
                            if processed[c] != nex:
                                return False
                        else:
                            s[nex].add(c)
                            queue.append(c)
                            processed[c] = nex
        return len(processed.keys()) == len(graph)
# O(V + E) for time and space.
