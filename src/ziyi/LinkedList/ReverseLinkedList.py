#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-03 23:45:45
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def createNode(nums):
	nodes = [ListNode(x) for x in nums]
	for i in range(len(nums)-1):
		nodes[i].next = nodes[i+1]
	print_list(nodes[0])
	return nodes[0]
def print_list(head):
	print 'List:',
	while head:
		print head.val,' ',
		head = head.next
	print ''
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
        	pivot = head 
        	frontier = None
        	while pivot and pivot.next:
        		frontier = pivot.next
        		pivot.next = pivot.next.next
        		frontier.next = head
        		head = frontier
        return head

def main():
	l = createNode([1,2,3,4,5])
	s = Solution()
	new_l = s.reverseList(l)
	print_list(new_l)

if __name__ == '__main__':
	main()