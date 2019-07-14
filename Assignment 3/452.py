class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)
        points.sort(key=lambda x: x[0], reverse=True)
        arrowX = points[0][0]
        result = 1
        for i in range(1, len(points)):
            if arrowX > points[i][1]:
                result += 1
                arrowX = points[i][0]
                
        return result
# O(NLog(N)) for time. O(1) for space.
