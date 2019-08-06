from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = Graph()
        for pair in prerequisites: # O(M) for time and space
            g.addEdge(pair[0], pair[1])
        prev = numCourses
        processed = set() # O(N) for space
        while prev > 0: # O(N^2) for worst case
            count = prev
            for i in range(numCourses):
                if i not in processed:
                    for c in g.graph[i]:
                        if c not in processed:
                            break
                    else:
                        processed.add(i)
                        count -= 1
            if prev == count:
                return False
            prev = count
        return True
