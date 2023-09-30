# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        counter = 0
        curr = head
        while curr:
            counter += 1
            curr = curr.next
        
        dummy = ListNode()
        dcurr = dummy
        curr = head
        for i in range(counter // k):
            for j in range(k):
                stack.append(curr)
                curr = curr.next
            for j in range(k):
                dcurr.next = stack.pop()
                dcurr = dcurr.next
        dcurr.next = curr
        return dummy.next