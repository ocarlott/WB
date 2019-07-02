class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        setNums1 = set(nums1) # O(N) for time and space
        result = set() # O(M) for space
        for n in nums2: # O(M)
            if n in setNums1:
                result.add(n)
        return list(result) # O(M)


# O(N + M) for time and space.
