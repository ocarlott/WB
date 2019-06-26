class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        row = len(A)
        col = len(A[0])
        offset = 0 if col % 2 == 0 else 1
        colRange = col // 2 + offset
        for ri in range(row):
            for ci in range(colRange):
                A[ri][ci], A[ri][col - 1 - ci] = 1 - A[ri][col - 1 - ci], 1 - A[ri][ci]
        return A
# O(mn) for time. O(1) for space
