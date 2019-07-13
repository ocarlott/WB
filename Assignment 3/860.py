from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        drawer = defaultdict(int)
        for payment in bills:
            if payment == 5:
                drawer[5] += 1
            elif payment == 10:
                if drawer[5] >= 1:
                    drawer[10] += 1
                    drawer[5] -= 1
                else:
                    return False
            else:
                if drawer[10] >= 1:
                    if drawer[5] >= 1:
                        drawer[10] -= 1
                        drawer[5] -= 1
                        drawer[20] += 1
                    else:
                        return False
                else:
                    if drawer[5] >= 3:
                        drawer[5] -= 3
                        drawer[20] += 1
                    else:
                        return False
        return True

# O(N) for time. O(1) for space
