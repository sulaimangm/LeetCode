# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        dummy = ListNode(next = head)
        curr = dummy
        while curr:
            stack.append(curr)
            curr = curr.next
        for i in range(n):
            popped = stack.pop()
        stack[-1].next = popped.next
        return dummy.next