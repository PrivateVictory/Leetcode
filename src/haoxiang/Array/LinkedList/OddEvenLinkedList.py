# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        node = head
        if node is None:
            return head

        lastOdd = head
        firstEven = head.next
        pre = head
        node = firstEven
        i = 2
        while node:
            if i % 2 != 0:
                lastOdd.next = node
                lastOdd = node
                pre.next = node.next
                node.next = firstEven
                node = pre.next
                i += 1
            else:
                i += 1
                pre = node
                node = node.next
        return head
