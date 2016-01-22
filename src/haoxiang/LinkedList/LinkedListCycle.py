# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur1 = cur2 = head
        while cur1 and cur1.next:
            cur1 = cur1.next.next
            cur2 = cur2.next
            if cur1 is cur2:
                return True
        return False
        # res = []
        # num = 0
        # while head:
        #     if head.val not in res:
        #         num+=1
        #     res.append(head.val)
        # if len(res) is num:
        #     return False
        # else:
        #     return True




        
