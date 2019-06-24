class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evenPtr = 0
        oddPtr = len(A) - 1
        while True:
            if evenPtr == oddPtr:
                return A
            if A[evenPtr] % 2 == 0:
                evenPtr += 1
            elif A[oddPtr] % 2 == 1:
                oddPtr -= 1
            else:
                A[oddPtr], A[evenPtr] = A[evenPtr], A[oddPtr]
# O(n) for time. O(1) for space.
