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
            if self.rank[parent1] < self.rank[parent2]:
                self.rank[parent2] += self.rank[parent1] + 1
                self.parent[parent1] = parent2
            else:
                self.rank[parent1] += self.rank[parent2] + 1
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
        uf = UnionFind(newGridRowCount * newGridColCount) # O(NM) time and space
        for row in range(newGridRowCount): # O(N)
            for col in range(newGridColCount): # O(M)
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
            
# O(N^2) for time and O(N^2) for space. This version extends the original grid to generalize how we check an element's neighbors

# Version 2

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowCount = len(grid)
        if rowCount == 0:
            return 0
        colCount = len(grid[0])
        uf = UnionFind(rowCount * colCount) # O(N^2) time and space
        
        def checkAndJoin(rowIndex, colIndex, position, offset):
            if grid[rowIndex][colIndex] == '1':
                uf.union(position, position + offset)
                
        for row in range(rowCount): # O(N^2)
            topSide = row == 0
            bottomSide = row == rowCount - 1
            above = row - 1
            below = row + 1
            for col in range(colCount):
                position = row * colCount + col
                if grid[row][col] == '1':
                    leftSide = col == 0
                    rightSide = col == colCount - 1
                    left = col - 1
                    right = col + 1
                    if rowCount > 1:
                        if topSide:
                            checkAndJoin(below, col, position, colCount)
                        elif bottomSide:
                            checkAndJoin(above, col, position, -colCount)
                        else:
                            checkAndJoin(below, col, position, colCount)
                            checkAndJoin(above, col, position, -colCount)
                    if colCount > 1:
                        if leftSide:
                            checkAndJoin(row, right, position, 1)
                        elif rightSide:
                            checkAndJoin(row, left, position, -1)
                        else:
                            checkAndJoin(row, right, position, 1)
                            checkAndJoin(row, left, position, -1)
                else:
                    uf.notExists(position)
        return uf.getGroups()
            
# O(NM) for time and O(NM) for space 
