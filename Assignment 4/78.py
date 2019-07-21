class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def getSubsets(nums, index):
            if len(nums) - index == 0:
                return [[]]
            lists = getSubsets(nums, index + 1)
            temp = []
            for ls in lists:
                nl = ls.copy()
                nl.append(nums[index])
                temp.append(nl)
            lists.extend(temp)
            return lists
        return getSubsets(nums, 0)
# O(n!) for time and space
