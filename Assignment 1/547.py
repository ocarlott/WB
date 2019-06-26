class UnionFind:
    def __init__(self, size):
        self.rank = [0 for x in range(size)] # O(N) for time and space
        self.parent = [x for x in range(size)]
        
    def find(self, el):
        path = []
        while self.parent[el] != el:
            path.append(el)
            el = self.parent[el]
        for item in path:
            self.parent[item] = el
        return el
            
    def union(self, e1, e2):
        p1 = self.find(e1)
        p2 = self.find(e2)
        if p1 != p2:
            if self.rank[p1] < self.rank[p2]:
                self.rank[p2] += self.rank[p1] + 1
                self.parent[p1] = p2
            else:
                self.rank[p1] += self.rank[p2] + 1
                self.parent[p2] = p1
                
    def getGroups(self):
        total = 0
        for i in range(len(self.parent)): # O(N)
            if self.parent[i] == i:
                total += 1
        return total

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        length = len(M)
        uf = UnionFind(length)
        for row in range(length): # (N - 1) + (N - 2) + .. + 1 = O(N^2)
            for col in range(row + 1, length):
                if M[row][col] == 1:
                    uf.union(row, col)
        return uf.getGroups()
        
# O(N^2) for time and space
