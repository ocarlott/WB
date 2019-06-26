class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        ref = ord("a")
        firstLetterCapital = ord(word[0]) < ref
        secondLetterCapital = False
        for i in range(len(word)):
            if i == 1:
                secondLetterCapital = ord(word[1]) < ref
                if secondLetterCapital and not firstLetterCapital:
                    return False
            elif i != 0:
                isCapital = ord(word[i]) < ref
                if isCapital != secondLetterCapital:
                    return False
        return True
# O(n) for time. O(1) for space
