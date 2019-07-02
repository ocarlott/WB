import string
from collections import defaultdict

lowercase = string.ascii_lowercase

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        codeSet = set()
        codeDict = {}
        for i in range(26):
            codeDict[lowercase[i]] = codes[i]
        for word in words: # O(N)
            wordTransformed = ""
            for c in word:  # O(M)
                wordTransformed += codeDict[c]
            codeSet.add(wordTransformed)
        return len(codeSet)

# O(NM) for time. O(N) for space
