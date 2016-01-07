__author__ = 'haoxiang'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next
        if head==None:
            return head
        temp=head.next
        prev=head
        while temp:
            if temp.val==val:
                prev.next=temp.next
            else:
                prev=temp
            temp=temp.next
        return head