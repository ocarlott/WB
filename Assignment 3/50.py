class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
    
        if n == 0:
            return 1
        else:
            re = n % 2
            div = n // 2
            powDiv = self.myPow(x, div)
            if re == 1:
                return x * powDiv * powDiv
            else:
                return powDiv * powDiv
            
# O(Log(N)) for time. O(1) for space.
