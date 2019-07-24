# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def preOrderTraverse(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            result = [root.val]
            if root.left:
                result.extend(preOrderTraverse(root.left))
            else:
                result.append(None)
            if root.right:
                result.extend(preOrderTraverse(root.right))
            return result
        ls1 = preOrderTraverse(p)
        ls2 = preOrderTraverse(q)
        if len(ls1) != len(ls2):
            return False
        for i in range(len(ls1)):
            if ls1[i] != ls2[i]:
                return False
        return True
# O(N) for time and space.
