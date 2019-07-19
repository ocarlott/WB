class Solution:
    def isValid(self, s: str) -> bool:
        stacks = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stacks.append(c)
            elif c == ")":
                if len(stacks) == 0 or stacks.pop() != "(":
                    return False
            elif c == "}":
                if len(stacks) == 0 or stacks.pop() != "{":
                    return False
            else:
                if len(stacks) == 0 or stacks.pop() != "[":
                    return False
        return len(stacks) == 0
# O(N) for time and space.
