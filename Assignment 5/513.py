# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return None
        def bfs(root, ls, q = deque()):
            if not root:
                ls.append(None)
                return
            ls.append(root.val)
            q.append(root.right)
            q.append(root.left)
            if q:
                bfs(q.popleft(), ls, q)
            if q:
                bfs(q.popleft(), ls, q)
        ls = []
        bfs(root, ls)
        while ls[-1] is None:
            ls.pop()
        return ls[-1]
