# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''dummy = ListNode(next = head)
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

        return dummy.next'''


        dummy = ListNode(next = head)
        prev = dummy
        curr = head
        last = dummy
        length = 0
        while last.next:
            last = last.next
            length += 1
        if length in [0,1]:
            return head
        
        for _ in range(length):
            if curr.val < x:
                prev = curr
                curr = curr.next
            else:
                last.next = curr
                prev.next = curr.next
                last = last.next
                curr = curr.next
                last.next = None
        
        return dummy.next

        