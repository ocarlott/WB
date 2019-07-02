import string

lowercase = string.ascii_lowercase

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        freq = {}
        codeDict = {}
        for i in range(26):
            codeDict[lowercase[i]] = codes[i]
        for word in words: # O(N)
            wordTransformed = ""
            for c in word:  # O(M)
                wordTransformed += codeDict[c]
            freq[wordTransformed] = freq.get(wordTransformed, 0)
        return len(freq.keys())

# O(NM) for time. O(N) for space
