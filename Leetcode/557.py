class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ");
        result = ""
        for wi in range(len(words)):
            wArr = list(words[wi])
            lastIndex = len(wArr) - 1
            for i in range(lastIndex // 2 + 1):
                wArr[i], wArr[lastIndex - i] = wArr[lastIndex - i], wArr[i]
            word = "".join(wArr)
            result = word if wi == 0 else result + " " + word
        return result
# O(n) for time. O(n) for space
