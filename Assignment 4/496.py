class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        dic = { nums1[i]:i for i in range(len(nums1)) }
        stack = []
        for i in range(len(nums2)):
            while len(stack) > 0 and stack[-1] < nums2[i]:
                temp = stack.pop()
                if temp in dic:
                    result[dic[temp]] = nums2[i]
            stack.append(nums2[i])
        return result
# O(N) for time. O(M) for space.
