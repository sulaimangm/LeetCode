# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursion
        '''output = []
        
        def inorder(root: Optional[TreeNode]):
            if not root:
                return
            
            inorder(root.left)
            output.append(root.val)
            inorder(root.right)

        inorder(root)
        return output'''

        stack = []
        output = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            output.append(root.val)
            root = root.right
        return output


            


        
