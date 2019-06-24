class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            canDivide3 = i % 3 == 0
            canDivide5 = i % 5 == 0
            if canDivide3 and canDivide5:
                result.append("FizzBuzz")
            elif canDivide3:
                result.append("Fizz")
            elif canDivide5:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
# O(n) for time. O(n) for space
