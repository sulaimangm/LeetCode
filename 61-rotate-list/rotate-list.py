# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        l = 0
        while curr:
            curr = curr.next
            l += 1
        for i in range(k%l):
            curr = head
            prev = None
            while curr and curr.next:
                prev = curr
                curr = curr.next
            if curr and prev:
                curr.next = head
                prev.next = None
                head = curr
        return head
