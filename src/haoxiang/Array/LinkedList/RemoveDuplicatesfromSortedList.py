# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pos = head
        while pos:
            while pos.next and pos.val == pos.next.val:
                pos.next = pos.next.next
            pos = pos.next
        return head
