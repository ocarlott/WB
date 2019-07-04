import string
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # We will have to make comparison between each word in paragraph to the banned list, so it's better to use a set for banned words to reduce the comparison cost down to O(1)
        bannedDict = set(banned) # O(M) for time and space
        table = str.maketrans(string.ascii_uppercase + "!?',;.", string.ascii_lowercase + "      ") # O(1)
        newP = paragraph.translate(table) # O(N)
        pArray = newP.split(" ") # O(N)
        counter = Counter(pArray) # O(N)
        highestCount = 0
        word = ""
        for key, value in counter.items(): # O(N)
            if key not in bannedDict and value > highestCount and key != "":
                highestCount = value
                word = key
        return word
        
# O(N + M) for time and space
