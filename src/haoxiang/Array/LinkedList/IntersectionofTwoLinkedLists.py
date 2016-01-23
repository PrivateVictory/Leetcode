# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        curA,curB = headA,headB
        while curA is not curB:
            curA = headB if curA is None else curA.next
            curB = headA if curB is None else curB.next
        return curA
