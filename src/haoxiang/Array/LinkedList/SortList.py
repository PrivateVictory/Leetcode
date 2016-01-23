# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # res = []
        # pos = head
        # while pos:
        #     res.append(head.val)
        #     pos = pos.next
        # res.sort()
        # for i in range(len(res)):
        #     pos.val = res[i]
        #     pos = pos.next
        # return head
        if head is None or head.next is None:
            return head
        mid = (head.val + head.next.val) / 2
        if head.val > head.next.val:
            lhead, rhead = head.next, head
        else:
            lhead, rhead = head, head.next
        lit, rit = lhead, rhead
        it = head.next.next
        while it is not None:
            if it.val > mid:
                rit.next = it
                rit = it
            else:
                lit.next = it
                lit = it
            it = it.next
        lit.next, rit.next = None, None
        lhead = self.sortList(lhead)
        rhead = self.sortList(rhead)
        it = lhead
        while it.next is not None:
            it = it.next
        it.next = rhead
        return lhead
