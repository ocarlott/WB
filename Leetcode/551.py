class Solution:
    def checkRecord(self, s: str) -> bool:
        record = {}
        lateConCount = 0
        for c in s:
            if c == 'L':
                if lateConCount == 2:
                    return False
                else:
                    lateConCount += 1
            else:
                lateConCount = 0
            record[c] = record.get(c, 0) + 1
        return record.get('A', 0) <= 1
# O(N) for time. O(1) for space.
