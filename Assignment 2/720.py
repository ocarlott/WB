from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.children = defaultdict(str)
        
class TrieTree:
    def __init__(self):
        self.root = TrieNode()
        self.root.isEndOfWord = True
    
    def insert(self, word):
        current = self.root
        for i in range(len(word)):
            if word[i] not in current.children:
                current.children[word[i]] = TrieNode()
            current = current.children[word[i]]
        current.isEndOfWord = True
        
    def search(self, word):
        current = self.root
        for i in range(len(word)):
            if word[i] not in current.children:
                return False
            current = current.children[word[i]]
        return current.isEndOfWord # Should we require user of this lib to add a word first before searching
    
    def searchEveryChar(self, word):
        current = self.root
        for i in range(len(word)):
            if word[i] not in current.children:
                return False
            current = current.children[word[i]]
        return current.isEndOfWord

class Solution:
    def longestWord(self, words: List[str]) -> str:
        tree = TrieTree()
        for word in words: # O(N)
            tree.insert(word) # O(M)
        result = []
        maxLength = 0
        for word in words: # O(N)
            if tree.searchEveryChar(word): # O(M)
                if len(word) > maxLength:
                    maxLength = len(word)
                    result = [word]
                elif len(word) == maxLength:
                    result.append(word)
        smallestWord = result[0]
        for word in result: # < O(N)
            if word < smallestWord:
                smallestWord = word
        return smallestWord
    
# O(NM) for time and space
