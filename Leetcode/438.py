from collections import Counter, defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        lengthP = len(p)
        counterP = Counter(p)
        counterSub = defaultdict(int)
        charCount = 0
        result = []
        leftEdge = 0
        while leftEdge < len(s) and not s[leftEdge] in counterP: # Leave out the unmatched left part
            leftEdge += 1
        if leftEdge > len(s) - len(p) + 1:
            return []
        # Start window sliding
        rightEdge = leftEdge
        # print(counterP)
        while rightEdge < len(s):
            char = s[rightEdge]
            if not char in counterP:
                charCount = 0
                counterSub = defaultdict(int)
                leftEdge = rightEdge = rightEdge + 1
            else:
                charCount += 1
                counterSub[char] += 1
                if counterSub[char] <= counterP[char]:
                    if charCount == lengthP:
                        result.append(leftEdge)
                        counterSub[s[leftEdge]] -= 1
                        charCount -= 1
                        leftEdge += 1
                elif counterSub[char] > counterP[char]:
                    while char != s[leftEdge]:
                        counterSub[s[leftEdge]] -= 1
                        leftEdge += 1
                        charCount -= 1
                    counterSub[s[leftEdge]] -= 1
                    leftEdge += 1
                    charCount -= 1
                # print(leftEdge, rightEdge, counterSub)
                rightEdge += 1
        return result

# O(N) for time for space.
