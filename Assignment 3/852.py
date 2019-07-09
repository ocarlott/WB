class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left = 0
        if A[left] > A[left + 1]:
            return left
        right = len(A) - 1
        if A[right] > A[right - 1]:
            return right
        mid = (left + right) // 2
        while True:
            if A[mid] >= A[mid - 1] and A[mid] >= A[mid + 1]:
                return mid
            if A[mid] >= A[mid - 1]:
                left = mid
            if A[mid] >= A[mid + 1]:
                right = mid
            mid = (left + right) // 2
            
# O(Log(N)) for time. O(1) for space.
