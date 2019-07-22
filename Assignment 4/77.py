class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ls = [1] * k
        ls.extend([0] * (n - k))
        lis = [x for x in range(1, n + 1)]
        result = []
        if n == k:
            return [lis]
        while True:
            temp = []
            for i in range(n):
                if ls[i] == 1:
                    temp.append(lis[i])
            result.append(temp)
            oneCount = 0
            for i in range(n - 1):
                if ls[i] == 1:
                    oneCount += 1
                if ls[i] == 1 and ls[i + 1] == 0:
                    oneCount -= 1
                    ls[i], ls[i + 1] = ls[i + 1], ls[i]
                    for j in range(i):
                        if oneCount > 0:
                            ls[j] = 1
                            oneCount -= 1
                        else:
                            ls[j] = 0
                    break
            else:
                break
        return result
