class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        length = len(strs)
        if length == 0 or len(strs[0]) == 0:
            return result
        if length == 1:
            return strs[0]
        currentCharIndex = 0
        while True: # O(m)
            currentChar = ""
            for i in range(length): # O(n)
                if len(strs[i]) == currentCharIndex:
                    return result
                if i == 0:
                    currentChar = strs[i][currentCharIndex]
                elif i == length - 1:
                    if currentChar == strs[i][currentCharIndex]:
                        result += currentChar
                    else:
                        return result
                else:
                    if currentChar != strs[i][currentCharIndex]:
                        return result
            currentCharIndex += 1
# O(mn) for time - n is length of string list and m is length of string in list. O(m) for space.
