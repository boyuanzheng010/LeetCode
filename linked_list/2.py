# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        pointer = dummy
        carry = 0
        # Iterate the whole
        while l1 or l2 or carry:
            temp = 0
            if l1 != None:
                temp += l1.val
                l1 = l1.next
            if l2 != None:
                temp += l2.val
                l2 = l2.next
            temp += carry
            pointer.next = ListNode(temp % 10, None)
            carry = temp // 10
            pointer = pointer.next

        return dummy.next