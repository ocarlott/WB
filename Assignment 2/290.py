class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        strList = str.split(" ") # O(N)
        if len(pattern) != len(strList):
            return False
        trans = {} # O(N) for space
        usedSet = set() # (N) for space
        for i in range(len(pattern)): # O(N)
            if pattern[i] in trans:
                if trans[pattern[i]] != strList[i]:
                    return False
            else:
                if strList[i] in usedSet:
                    return False
                else:
                    trans[pattern[i]] = strList[i]
                    usedSet.add(strList[i])
        return True

# O(N) for time and space.
