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
        length = 0
        while curr:
            curr = curr.next
            length += 1
        k = k % length
        r = head
        l = head
        for i in range(k):
            r = r.next
        
        while r.next:
            r = r.next
            l = l.next
        
        r.next = head
        head = l.next
        l.next = None

        return head
