class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stacks = []
        for c in S:
            if c == "(":
                stacks.append(c)
            else:
                score = 0
                while stacks[-1] != "(":
                    score += stacks.pop()
                stacks.pop()
                score *= 2
                score = 1 if score == 0 else score
                stacks.append(score)
        return sum(stacks)
# O(N) for time and space.
