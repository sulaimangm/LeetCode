# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        diff = float('inf')
        prev = None
        '''stack = []
        output = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            #print(root.val)
            if prev is not None:
                diff = min(diff, abs(root.val - prev))
            prev = root.val
            root = root.right
        return diff'''

        def inorder(root):
            if not root:
                return
            nonlocal prev, diff
            inorder(root.left)
            if prev is not None:
                diff = min(diff, abs(root.val - prev))
            prev = root.val
            inorder(root.right)

        inorder(root)
        return diff