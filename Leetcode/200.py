class UnionFind:
    def __init__(self, size):
        self.rank = [0 for x in range(size)] # Initialize with size to prevent size scaling. O(N)
        self.parent = [x for x in range(size)]

    def find(self, el):
        path = []
        while self.parent[el] != el:
            path.append(el)
            el = self.parent[el]
        for item in path: # Path compression
            self.parent[item] = el
        return el
    
    def union(self, el1, el2):
        parent1 = self.find(el1)
        parent2 = self.find(el2)
        if parent1 != parent2:
            if self.parent[parent1] < self.parent[parent2]:
                self.rank[parent2] += self.rank[parent1]
                self.parent[parent1] = parent2
            elif self.parent[parent1] >= self.parent[parent2]:
                self.rank[parent1] += self.rank[parent2]
                self.parent[parent2] = parent1
    
    def notExists(self, index):
        self.parent[index] = -1
    
    def getGroups(self):
        total = 0
        for i in range(len(self.parent)):
            if self.parent[i] == i:
                total += 1
        return total
        
# Version 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowCount = len(grid)
        if rowCount == 0:
            return 0
        colCount = len(grid[0])
        newGridRowCount = rowCount + 2
        newGridColCount = colCount + 2
        newGrid = [[0 for x in range(newGridColCount)] for x in range(newGridRowCount)] # O(N)
        for row in range(rowCount): # O(N^2)
            for col in range(colCount):
                newGrid[row + 1][col + 1] = grid[row][col]
        uf = UnionFind(newGridRowCount * newGridColCount) # O(N^2) time and space
        for row in range(newGridRowCount): # O(N^2)
            for col in range(newGridColCount):
                position = row * newGridColCount + col
                if row > 0 and col > 0 and row < newGridRowCount - 1 and col < newGridColCount - 1 and newGrid[row][col] == '1':
                    uf.union(position, position)
                    if newGrid[row - 1][col] == '1':
                        uf.union(position, position - newGridColCount)
                    if newGrid[row + 1][col] == '1':
                        uf.union(position, position + newGridColCount)
                    if newGrid[row][col - 1] == '1':
                        uf.union(position, position - 1)
                    if newGrid[row][col + 1] == '1':
                        uf.union(position, position + 1)
                else:
                    uf.notExists(position)
        return uf.getGroups()
            
# O(N^2) for time and O(N^2) for space. This version extends the original grid to generalize 

# Version 2

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowCount = len(grid)
        if rowCount == 0:
            return 0
        colCount = len(grid[0])
        uf = UnionFind(rowCount * colCount) # O(N^2) time and space
        for row in range(rowCount): # O(N^2)
            topSide = row == 0
            bottomSide = row == rowCount - 1
            above = row - 1
            below = row + 1
            for col in range(colCount): # O(N^2)
                position = row * colCount + col
                if grid[row][col] == '1':
                    leftSide = col == 0
                    rightSide = col == colCount - 1
                    left = col - 1
                    right = col + 1
                    if rowCount > 1:
                        if topSide:
                            if grid[below][col] == '1':
                                uf.union(position, position + colCount)
                        elif bottomSide:
                            if grid[above][col] == '1':
                                uf.union(position, position - colCount)
                        else:
                            if grid[below][col] == '1':
                                uf.union(position, position + colCount)
                            if grid[above][col] == '1':
                                uf.union(position, position - colCount)
                    if colCount > 1:
                        if leftSide:
                            if grid[row][right] == '1':
                                uf.union(position, position + 1)
                        elif rightSide:
                            if grid[row][left] == '1':
                                uf.union(position, position - 1)
                        else:
                            if grid[row][right] == '1':
                                uf.union(position, position + 1)
                            if grid[row][left] == '1':
                                uf.union(position, position - 1)
                else:
                    uf.notExists(position)
        return uf.getGroups()
            
# O(N^2) for time and O(N^2) for space 
