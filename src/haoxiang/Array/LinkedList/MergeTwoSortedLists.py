# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2: return None
        elif not l1: return l2
        elif not l2: return l1

        l1Node = l1
        l2Node = l2

        res = ListNode(None)
        num = res
        while l1Node and l2Node:
            if l1Node.val<l2Node.val:
                res.next = l1Node
                l1Node = l1Node.next
                res = res.next
            else:
                res.next = l2Node
                l2Node = l2Node.next
                res = res.next
        if l1Node:
            res.next = l1Node
        if l2Node:
            res.next = l2Node

        return num.next
