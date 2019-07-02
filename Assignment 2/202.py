class Solution:
    def isHappy(self, n: int) -> bool:
        numSet = set()
        
        def isHappy(num):
            total = 0
            while (num > 0):
                re = num % 10
                num = num // 10
                total += re * re
            if total == 1:
                return True
            elif total in numSet:
                return False
            else:
                numSet.add(total)
                return isHappy(total)
        
        return isHappy(n)

# Unknown time complexity. O(n) for space
