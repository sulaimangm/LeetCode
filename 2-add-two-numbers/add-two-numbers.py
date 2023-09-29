# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sums = 0
        output = ListNode()
        temp = output
        while l1 and l2:
            sums += l1.val + l2.val
            temp.val = sums % 10
            sums = sums // 10
            l1 = l1.next
            l2 = l2.next
            if l1 or l2:
                temp.next = ListNode()
                temp = temp.next
            
        while l1:
            sums += l1.val
            temp.val = sums % 10
            sums = sums // 10
            l1 = l1.next
            if l1:
                temp.next = ListNode()
                temp = temp.next
        while l2:
            sums += l2.val
            temp.val = sums % 10
            sums = sums // 10
            l2 = l2.next
            if l2:
                temp.next = ListNode()
                temp = temp.next
        print(sums)

        if sums > 0:
            temp.next = ListNode()
            temp = temp.next
            temp.val = 1
        return output
