import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        boxSets = [] # O(N^2) for space
        colSets = [] # O(N^2) for space
        n = int(math.sqrt(length)) # O(Log(N))
        for i in range(length): # O(N)
            boxSets.append(set())
            colSets.append(set())
        for row in range(length): # O(N)
            rowSet = set() # O(N)
            for col in range(length): # O(N)
                current = board[row][col]
                x = row // n # If we see the board as x-y coordinates with unit as the length of each box, the top left box is at (0, 0) and bottom right box is at (2, 2). Therefore, we just need to divide current row and col values to get x, y coordinates for each box and compute the index from the coordinates.
                y = col // n
                boxIndex = x * n + y
                if current != ".":
                    if current in rowSet or current in colSets[col] or current in boxSets[boxIndex]:
                        return False
                    else:
                        rowSet.add(current)
                        colSets[col].add(current)
                        boxSets[boxIndex].add(current)
        return True
                   
# O(N^2) for time and space.
