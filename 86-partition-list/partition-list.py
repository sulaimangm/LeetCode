# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        less = []
        greater = []

        curr = head
        while curr:
            if curr.val < x:
                less.append(curr)
            else:
                greater.append(curr)
            curr = curr.next
        
        curr = dummy
        for i in less:
            curr.next = i
            curr = curr.next

        for i in greater:
            curr.next = i
            curr = curr.next
        
        curr.next = None

        return dummy.next
        