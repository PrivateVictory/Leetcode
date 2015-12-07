__author__ = 'haoxiang'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        pre = None
        while head:
            curr = head
            head = head.next
            curr.next = pre
            pre = curr
        return pre
