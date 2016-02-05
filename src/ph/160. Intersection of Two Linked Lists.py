# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pointA,pointB=headA,headB
        while pointA is not pointB:
        	pointA=headB if pointA==None else pointA.next
        	pointB=headA if pointB==andNone else pointB.next
        return pointA
















        # indicatorA=headA
        # indicatorB=headB
        # intersectionNode=None
        # while indicatorA !=None and indicatorB !=None:
        # 	if intersectionNode !=None:
        # 		if indicatorA.val !=indicatorB.c=val:
        # 			intersectionNode=None
        # 	else:
        # 		if indicatorA.val ==indicatorB.c=val:
        # 			intersectionNode=indicatorA
        # 	indicatorA=indicatorA.next
        # 	indicatorB=indicatorB.next
        # return intersectionNode