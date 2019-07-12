class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        sortedInt = sorted(intervals, key=lambda x: x[0]) # O(NLog(N)) for time. O(N) for space
        stack = []
        stack.append(sortedInt[0][0])
        stack.append(sortedInt[0][1])
        for index in range(1, len(sortedInt)): # O(N)
            if sortedInt[index][0] <= stack[-1]:
                if sortedInt[index][1] > stack[-1]:
                    stack.pop()
                    stack.append(sortedInt[index][1])
            else:
                stack.append(sortedInt[index][0])
                stack.append(sortedInt[index][1])
        result = []
        index = 0
        while index < len(stack): # O(N)
            result.append([stack[index], stack[index + 1]])
            index += 2
        return result
    
# O(NLog(N)) for time. O(N) for space.
