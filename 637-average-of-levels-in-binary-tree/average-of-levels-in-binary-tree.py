# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        output = []
        queue = deque([root])
        while queue:
            output.append(sum([node.val for node in queue])/len(queue))
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left) 
                if curr.right:
                    queue.append(curr.right) 
        return output