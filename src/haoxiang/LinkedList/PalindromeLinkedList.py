# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print res
        lens = len(res)
        # if res is []:
        #     return False
        for i in range(lens):
            if res[i] != res[lens-1-i]:
                return False
        return True
