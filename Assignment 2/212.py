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
        
    def search(self, word):
        current = self.root
        for c in word:
            if not c in current.children:
                return 0
            current = current.children[c]
        if current.isEndOfWord:
            return 2
        else:
            return 1
        
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        maxWordLength = 0
        for word in words: # O(K*L) for time and space
            if len(word) > maxWordLength:
                maxWordLength = len(word)
            trie.insert(word)
        rowCount = len(board)
        colCount = len(board[0])
        g = Graph() # O(N*M) for space
        result = set()
        letterList = [] # O(N* M) for space
        for row in range(rowCount): # O(NM)
            for col in range(colCount):
                letterList.append(board[row][col])
        def dfs(v, visited, wordList):
            nonlocal trie, g, letterList
            if v in visited:
                return False
            visited.add(v)
            wordList.append(letterList[v])
            word = "".join(wordList)
            search = trie.search(word)
            if search == 0:
                return True # Return true because vertice has been added to processing list
            elif search == 2:
                result.add(word)
            if len(wordList) >= maxWordLength:
                return True
            for index, item in enumerate(g.graph[v]): # O(1)
                if dfs(item, visited, wordList):
                    visited.remove(item)
                    wordList.pop()
            return True # After we are done with a node, return true so the caller can remove this node value.
                    
        
        for row in range(rowCount): # O(NM)
            for col in range(colCount):
                top = row == 0
                left = col == 0
                bottom = row == rowCount - 1
                right = col == colCount - 1
                if not top:
                    g.addEdge(row * colCount + col, (row - 1) * colCount + col)
                if not bottom:
                    g.addEdge(row * colCount + col, (row + 1) * colCount + col)
                if not left:
                    g.addEdge(row * colCount + col, row * colCount + col - 1)
                if not right:
                    g.addEdge(row * colCount + col, row * colCount + col + 1)
                    
        for row in range(rowCount): # O(N)
            for col in range(colCount): # O(M)
                dfs(row * colCount + col, set(), []) # O(3^L) for time. Total of O(N*M*3^L) for time. O(L) for space.
                
        return list(result)
           
# O(N*M*3^L + K*L) for time. O(N*M + L) = O(N*M) for space. (L < N*M)
