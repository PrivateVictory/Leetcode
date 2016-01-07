#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-05 13:41:18
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
        	return 0
        else:
        	return self.iterDepth(1, [root])

    def iterDepth(self, depth, nodeList):
    	newList = []
    	for node in nodeList:
    		if_leaf = True
    		if node.left:
    			newList.append(node.left)
    			if_leaf = False
    		if node.right:
    			newList.append(node.right)
    			if_leaf = False
    		if if_leaf:
    			return depth
    	return self.iterDepth(depth+1, newList)