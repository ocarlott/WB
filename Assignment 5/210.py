from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = Graph()
        stack = []
        processed = set()
        for pair in prerequisites:
            g.addEdge(pair[0], pair[1])
        coursesLeft = numCourses
        while coursesLeft > 0:
            count = coursesLeft
            for i in range(numCourses):
                if i not in processed:
                    for c in g.graph[i]:
                        if c not in processed:
                            break
                    else:
                        processed.add(i)
                        stack.append(i)
                        count -= 1
            if count == coursesLeft:
                return
            coursesLeft = count
        return stack        
