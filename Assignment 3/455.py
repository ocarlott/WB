class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(g) == 0 or len(s) == 0:
            return 0
        g.sort()
        s.sort()
        print(g)
        print(s)
        result = 0
        cIndex = 0
        for c in g:
            while cIndex < len(s) and c > s[cIndex]:
                cIndex += 1
            if cIndex >= len(s):
                break
            else:
                result += 1
                cIndex += 1
        return result
# O(NLog(N) + MLog(M)) for time. O(1) for space.
