from collections import defaultdict

class Node:
    def __init__(self):
        self.isEndOfWord = False
        self.children = defaultdict(str)

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for char in word:
            if not char in current.children:
                current.children[char] = Node()
            current = current.children[char]
        current.isEndOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for char in word:
            if not char in current.children:
                return False
            current = current.children[char]
        return current.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for char in prefix:
            if not char in current.children:
                return False
            current = current.children[char]
        return True
