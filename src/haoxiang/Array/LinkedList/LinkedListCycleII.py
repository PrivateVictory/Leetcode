# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pos = cur1 = cur2 = head
        while cur1 and cur1.next:
            cur1 = cur1.next.next
            cur2 = cur2.next
            if cur1 is cur2:
                while pos is not cur2:
                    pos = pos.next
                    cur2 = cur2.next
                return pos
        return None
        # res = {}
        # pos = head
        # while pos:
        #     if pos not in res:
        #         res[pos] = 1
        #         pos = pos.next
        #     else:
        #         return pos
        # return None
