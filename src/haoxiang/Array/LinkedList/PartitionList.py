# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        res1 = []
        res2 = []
        pos = head
        cur = head
        while pos:
            if pos.val < x:
                res1.append(pos.val)
            else:
                res2.append(pos.val)
            pos = pos.next
        for i in range(len(res1)):
            cur.val = res1[i]
            cur = cur.next
        for j in range(len(res2)):
            cur.val = res2[j]
            cur = cur.next
        return head
