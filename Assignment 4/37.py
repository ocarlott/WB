st = "123456789"

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        empties = []
        n = len(board)
        m = 1
        while m * m < n:
            m += 1
        blockSets = [set() for i in range(n)]
        rowSets = [set() for i in range(n)]
        colSets = [set() for i in range(n)]
        for r in range(n):
            for c in range(n):
                cur = board[r][c]
                if cur == ".":
                    empties.append((r, c))
                else:
                    rowSets[r].add(cur)
                    colSets[c].add(cur)
                    blockSets[(r // m) * m + (c // m)].add(cur)
        self.solve(board, m, empties[::-1], rowSets, colSets, blockSets)
            
    def solve(self, board, m, empties, rowSets, colSets, blockSets):
        if len(empties) == 0:
            return True
        for i in range(len(board)):
            (r, c) = empties.pop()
            board[r][c] = st[i]
            blockIndex = (r // m) * m + (c // m)
            if self.isValid(board, blockIndex, r, c, rowSets, colSets, blockSets):
                rowSets[r].add(st[i])
                colSets[c].add(st[i])
                blockSets[blockIndex].add(st[i])
                if self.solve(board, m, empties, rowSets, colSets, blockSets):
                    return True
                rowSets[r].remove(st[i])
                colSets[c].remove(st[i])
                blockSets[blockIndex].remove(st[i])
            empties.append((r, c))
            board[r][c] = "."
        return False
    
    def isValid(self, board, blockIndex, row, col, rowSets, colSets, blockSets):
        temp = board[row][col]
        return temp not in rowSets[row] and temp not in colSets[col] and temp not in blockSets[blockIndex]
    
