class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1): # O(n) here
            remaining = num
            while remaining > 0: # O(logn) here
                digit = remaining % 10
                remaining //= 10
                if digit == 0 or num % digit != 0:
                    break
                elif num % digit == 0 and remaining == 0:
                    result.append(num)
        return result
# O(nlogn) for time. O(n) for space.
