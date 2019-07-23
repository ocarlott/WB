paDict = { 0: [""], 1: ["()"] }

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n in paDict:
            return paDict[n]
        result = []
        for i in range(n):
            x = self.generateParenthesis(i)
            y = self.generateParenthesis(n - i - 1)
            for xs in x:
                for ys in y:
                    result.append(f"({xs}){ys}")
        return result
    
table = { 0: [""] }

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return table[0]
        for i in range(1, n + 1):
            temp = []
            for a in range(i):
                for x in table[a]:
                    for y in table[i - a - 1]:
                        temp.append(f"({x}){y}")
            table[i] = temp
        return table[n]
    
