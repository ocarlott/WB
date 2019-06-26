class UnionFind:
    def __init__(self, size):
        self.rank = [0 for x in range(size)] # O(N)
        self.parent = [x for x in range(size)]
        
    def find(self, el):
        path = []
        while self.parent[el] != el:
            path.append(el)
            el = self.parent[el]
        for item in path:
            self.parent[item] = el
        return el
    
    def union(self, el1, el2):
        p1 = self.find(el1)
        p2 = self.find(el2)
        if p1 != p2:
            if self.rank[p1] < self.rank[p2]:
                self.rank[p2] += self.rank[p1] + 1
                self.parent[p1] = p2
            else:
                self.rank[p1] += self.rank[p2] + 1
                self.parent[p2] = p1
                
    def isConnected(self, el1, el2):
        return self.find(el1) == self.find(el2)
                
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowCount = len(board)
        if rowCount > 2:
            colCount = len(board[0])
            if colCount > 2:
                size = rowCount * colCount
                uf = UnionFind(size + 4) # 4 extra virtual nodes for 4 edges. # O(MN)
                topVirtualNodeIndex = size
                rightVirtualNodeIndex = size + 1
                bottomVirtualNodeIndex = size + 2
                leftVirtualNodeIndex = size + 3
                
                def checkAndJoin(rowIndex, colIndex, position, offset):
                    if board[rowIndex][colIndex] == 'O':
                        uf.union(position, position + offset)
                        
                for row in range(rowCount): # O(N)
                    topEdge = row == 0
                    bottomEdge = row == rowCount - 1
                    above = row - 1
                    below = row + 1
                    for col in range(colCount): # O(M)
                        if board[row][col] == 'O':
                            leftEdge = col == 0
                            rightEdge = col == colCount - 1
                            left = col - 1
                            right = col + 1
                            position = row * colCount + col
                            if topEdge:
                                uf.union(position, topVirtualNodeIndex)
                                checkAndJoin(below, col, position, colCount)
                            elif bottomEdge:
                                uf.union(position, size + 2)
                                checkAndJoin(above, col, position, -colCount)
                            else:
                                checkAndJoin(below, col, position, colCount)
                                checkAndJoin(above, col, position, -colCount)
                            if rightEdge:
                                uf.union(position, size + 1)
                                checkAndJoin(row, left, position, -1)
                            elif leftEdge:
                                uf.union(position, size + 3)
                                checkAndJoin(row, right, position, 1)
                            else:
                                checkAndJoin(row, left, position, -1)
                                checkAndJoin(row, right, position, 1)
                for row in range(rowCount): # O(N)
                    for col in range(colCount): # O(M)
                        position = row * colCount + col
                        if not (uf.isConnected(position, topVirtualNodeIndex) or uf.isConnected(position, rightVirtualNodeIndex) or uf.isConnected(position, bottomVirtualNodeIndex) or uf.isConnected(position, leftVirtualNodeIndex)):
                            board[row][col] = 'X'
                            
# O(MN) for time. O(MN) for space
