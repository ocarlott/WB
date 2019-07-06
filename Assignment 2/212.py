from collections import defaultdict

class Node:
    def __init__(self):
        self.isEndOfWord = False
        self.children = defaultdict(str)
   
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        current = self.root
        for c in word:
            if not c in current.children:
                current.children[c] = Node()
            current = current.children[c]
        current.isEndOfWord = True
        
    def search(self, word): # O(len(word))
        current = self.root
        for c in word:
            if not c in current.children:
                return False
            current = current.children[c]
        return current.isEndOfWord
    
    def searchPrefix(self, word): # O(len(word))
        current = self.root
        for c in word:
            if not c in current.children:
                return False
            current = current.children[c]
        return True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words: # O(K)
            trie.insert(word)
        rowCount = len(board)
        colCount = len(board[0])
        
        def getNeighbors(coord, usedBoxes): # O(1)
            row, col = coord
            nonlocal rowCount, colCount
            top = row == 0
            left = col == 0
            bottom = row == rowCount - 1
            right = col == colCount - 1
            neighbors = []
            if not top:
                if not ((row - 1) * colCount + col) in usedBoxes:
                    neighbors.append((row - 1, col))
            if not bottom:
                if not ((row + 1) * colCount + col) in usedBoxes:
                    neighbors.append((row + 1, col))
            if not left:
                if not (row * colCount + (col - 1)) in usedBoxes:
                    neighbors.append((row, col - 1))
            if not right:
                if not (row * colCount + (col + 1)) in usedBoxes:
                    neighbors.append((row, col + 1))
            return neighbors
           
        result = set()
        
        def backtrack(coord, usedTupleList, usedBoxes):
            row, col = coord
            nonlocal trie, board, rowCount, colCount, result
            usedTupleList.append((row, col))
            usedBoxes.add(row * colCount + col)
            wordArr = []
            for coord in usedTupleList:
                wordArr.append(board[coord[0]][coord[1]])
            word = "".join(wordArr) # < O(L)
            if not trie.searchPrefix(word): # < O(L)
                usedTupleList.pop()
                usedBoxes.remove(row * colCount + col)
                return
            if trie.search(word): # < O(L)
                result.add(word)
                # usedTupleList.pop()
                # usedBoxes.remove(row * colCount + col)
                # return
            neighbors = getNeighbors((row, col), usedBoxes)
            if len(neighbors) == 0:
                return
            for neighbor in neighbors:
                cpTupleList = usedTupleList.copy() # O(L)
                cpSet = usedBoxes.copy() # O(L)
                backtrack(neighbor, cpTupleList, cpSet)
        
        for row in range(rowCount): # For the backtrack function, we can think that for each element picked, we have at most 4 options to pick the next element. So the upperbound will be O(4^(NM)).
            for col in range(colCount):
                usedTupleList = []
                usedBoxes = set()
                backtrack((row, col), usedTupleList, usedBoxes)
        return list(result)
    
# Word length: L, Width: N, Height: M, Words: K
# O(L*4^(MN)) for time and space.
