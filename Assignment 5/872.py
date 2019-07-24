# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def getSequence(root):
            if not root.left and not root.right:
                return [root.val]
            result = []
            if root.left:
                result.extend(getSequence(root.left))
            if root.right:
                result.extend(getSequence(root.right))
            return result
        
        ls1 = getSequence(root1)
        ls2 = getSequence(root2)
        if len(ls1) != len(ls2):
            return False
        for i in range(len(ls1)):
            if ls1[i] != ls2[i]:
                return False
        return True
    
# O(N) for time and space.
