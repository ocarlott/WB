class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        setNums1 = set(nums1) # O(N) for time and space
        setNums2 = set(nums2) # O(M) for space
        result = setNums1.intersection(setNums2)
        return list(result) # O(M)


# O(N + M) for time and space.
