# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive
        '''output = []
        if not root:
            return output

        def preorder(root):
            if not root:
                return 
            output.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return output'''

        # Iterative
        output = []
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                output.append(root.val)
                root = root.left
            root = stack.pop()
            root = root.right
        
        return output