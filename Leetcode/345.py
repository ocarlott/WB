class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"e", "i", "a", "u", "o", "E", "I", "A", "U", "O"}
        left = 0
        st = list(s)
        length = len(st)
        right = length - 1
        while True:
            if right - left <= 0:
                break
            if st[left] not in vowels:
                left += 1
            if st[right] not in vowels:
                right -= 1
            if st[left] in vowels and st[right] in vowels:
                st[left], st[right] = st[right], st[left]
                left += 1
                right -= 1
        return "".join(st)
# O(n) for time. O(n) for space
