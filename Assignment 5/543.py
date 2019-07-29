# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(root):
            if not root:
                return 0, 0
            lCount, lHigh = dfs(root.left)
            rCount, rHigh = dfs(root.right)
            return (max(lCount, rCount) + 1, max(lHigh, rHigh, lCount + rCount + 1))
        (count, high) = dfs(root)
        return max(count, high) - 1
