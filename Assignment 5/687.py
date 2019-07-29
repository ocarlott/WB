# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(root):
            if not root:
                return (None, 0, 0)
            value, count = root.val, 0
            (lValue, lCount, lHigh) = dfs(root.left)
            (rValue, rCount, rHigh) = dfs(root.right)
            if lValue != value:
                lCount = 0
            if rValue != value:
                rCount = 0
            count = lCount + rCount + 1
            return (value, max(lCount, rCount) + 1, max(lHigh, rHigh, count))
        (value, count, high) = dfs(root)
        return max(count, high) - 1
