class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stacks = []
        for c in ops:
            if c == "C":
                stacks.pop()
            elif c == "D":
                stacks.append(2 * stacks[-1])
            elif c == "+":
                stacks.append(stacks[-1] + stacks[-2])
            else:
                stacks.append(int(c))
        return sum(stacks)
# O(N) for time and space.
