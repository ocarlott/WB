"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = []
        for c in root.children:
            result.extend(self.postorder(c))
        result.append(root.val)
        return result

# O(N) for time and space.
