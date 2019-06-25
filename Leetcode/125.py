class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        length = len(s)
        right = length - 1
        while True:
            if right - left <= 0:
                return True
            while not s[left].isalnum():
                left += 1
                if left == length:
                    return True
            while not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
# O(n) for time. O(1) for space.
