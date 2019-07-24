class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        maximum = 0
        total = 0
        for n in nums:
            total += n
            maximum = n if n > maximum else maximum
        if total % k != 0 or maximum > total // k:
            return False
        target = total // k
        numDict = {i:nums[i] for i in range(len(nums))}
        
        def solve(n, k, index, numDict, subSum, target):
            if k == 0:
                return True
            if target == subSum: 
                return solve(n, k - 1, 0, numDict, 0, target)
            for i in range(index, n):
                if i in numDict and target >= subSum + numDict[i]:
                    temp = numDict[i]
                    del numDict[i]
                    if solve(n, k, i + 1, numDict, subSum + temp, target):
                        return True
                    numDict[i] = temp
            return False  
        
        return solve(len(nums), k, 0, numDict, 0, target)
