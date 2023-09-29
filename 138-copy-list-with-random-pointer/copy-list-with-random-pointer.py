"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        random = {None: None}
        curr = head
        while curr:
            temp = Node(curr.val)
            random[curr] = temp
            curr = curr.next

        curr = head
        while curr:
            copy = random[curr]
            copy.next = random[curr.next]
            copy.random = random[curr.random]
            curr = curr.next

        return random[head]

        