# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        res = dummy
        total = 0
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            total = carry

            if l1 is not None:
                total += l1.val
                l1 = l1.next
            
            if l2 is not None:
                total += l2.val
                l2 = l2.next

            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next

        return res.next