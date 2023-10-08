"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = deque([root])
        temp = None
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    if not temp:
                        temp = curr.left
                    else:
                        temp.next = curr.left
                        temp = curr.left
                    queue.append(curr.left)
                if curr.right:
                    if not temp:
                        temp = curr.right
                    else:
                        temp.next = curr.right
                        temp = curr.right
                    queue.append(curr.right)
            temp = None

        return root    
            
            
