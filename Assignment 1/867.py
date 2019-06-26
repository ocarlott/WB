class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row = len(A)
        col = len(A[0])
        B = []
        for rowIndex in range(col):
            C = []
            for colIndex in range(row):
                C.append(A[colIndex][rowIndex])
            B.append(C)
        return B
# O(mn) for time. O(mn) for space.
