# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """ 
        lst = []
        if not root:
            return None

        def preorder(root):
            if not root:
                return 
            lst.append(root)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        
        for i in range(len(lst)-1):
            lst[i].right = lst[i+1]
            lst[i].left = None

        