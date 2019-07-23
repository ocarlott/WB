st = "123456789"

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        empties = set()
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    empties.add((r, c))
        self.solve(board, empties)
            
    def solve(self, board, empties):
        r, c = self.getEmptyCell(board)
        if r == -1 and c == -1:
            return True
        for i in range(len(board)):
            board[r][c] = st[i]
            if self.isValid(board, r, c):
                if self.solve(board):
                    return True
            board[r][c] = "."
        return False
    
    def isValid(self, board, row, col):
        n = len(board)
        m = 1
        while m * m < n:
            m += 1
        rowSet = set()
        colSet = set()
        blockSet = set()
        for i in range(n):
            if board[row][i] in rowSet or board[i][col] in colSet:
                return False
            if board[row][i] != ".":
                rowSet.add(board[row][i])
            if board[i][col] != ".":
                colSet.add(board[i][col])
        for i in range((row // m) * m, (row // m) * m + m):
            for j in range((col // m) * m, (col // m) * m + m):
                if board[i][j] in blockSet:
                    return False
                if board[i][j] != ".":
                    blockSet.add(board[i][j])
        return True
