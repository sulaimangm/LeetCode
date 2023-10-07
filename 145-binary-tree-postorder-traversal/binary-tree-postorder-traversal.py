# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursion
        '''output = []
        if not root:
            return output

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            output.append(root.val)
        
        postorder(root)
        return output'''

        # Iterative DFS
        output = []
        stack = []

        while stack or root:
            while root:
                stack.append((root, False))
                root = root.left

            node, visited = stack.pop()
            if visited:
                output.append(node.val)
            else:
                stack.append((node, True))
                root = node.right

        return output
            
            