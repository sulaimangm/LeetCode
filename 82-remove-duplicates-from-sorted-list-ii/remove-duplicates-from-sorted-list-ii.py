# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''dummy = ListNode(next = head)
        prev = dummy
        duplicate = False
        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
                duplicate = True
            if duplicate:
                head = head.next
                prev.next = head
                duplicate = False
            else:
                head = head.next
                prev = prev.next
        return dummy.next'''


        dummy = ListNode(next = head)
        prev = dummy
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                prev.next = head
            else:
                head = head.next
                prev = prev.next
        return dummy.next




