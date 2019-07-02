class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        usedSet = set() # O(N) for space
        translateMap = {} # O(N) for space
        translated = "" # O(N) for space
        for i in range(len(t)): # O(N)
            if t[i] in translateMap:
                translated += translateMap[t[i]]
            else:
                if s[i] in usedSet:
                    return False
                else:
                    translateMap[t[i]] = s[i]
                    usedSet.add(s[i])
                    translated += s[i]
        return translated == s # O(N)
    
# O(N) for time and space.
