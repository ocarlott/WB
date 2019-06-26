class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        for i in range(-1, -1 - length, -1): # O(n)
            if (digits[i] + 1) // 10 == 0:
                digits[i] = (digits[i] + 1) % 10
                break
            elif i == -length:
                digits[i] = (digits[i] + 1) % 10
                digits.insert(0, 1) # This is O(n) but happens only once
                break
            digits[i] = (digits[i] + 1) % 10
        return digits
# O(n) for time. O(1) for space.
