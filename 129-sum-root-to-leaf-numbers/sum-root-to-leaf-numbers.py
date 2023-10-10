# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        numbers = []

        def sums(root, num):
            if not root:
                return 
            num = num * 10 + root.val
            if not root.left and not root.right:
                numbers.append(num)
            sums(root.left, num)
            sums(root.right, num)

        sums(root, 0)

        sum = 0
        for i in numbers:
            sum += i
        return sum