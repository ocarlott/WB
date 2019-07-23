class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def solve(ls, result, index, working, target):
            if target == 0:
                return True
            if target < 0:
                return False
            for i in range(index, len(ls)):
                working.append(ls[i])
                if solve(ls, result, i, working, target - ls[i]):
                    result.append(working.copy())
                working.pop()
        solve(candidates, result, 0, [], target)
        return result
