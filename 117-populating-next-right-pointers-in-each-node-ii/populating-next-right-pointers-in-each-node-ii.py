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
        nxt = []

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    nxt.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    nxt.append(curr.right)
            for i in range(len(nxt)-1):
                if nxt[i+1]:
                    nxt[i].next = nxt[i+1]
            nxt = []

        return root    
            
            
