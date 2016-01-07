#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-05 13:18:43
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
        	return 0
        else:
        	return self.iterDepth(0,[root])
        

    def iterDepth(self, depth, nodeList):
    	if len(nodeList) == 0:
    		return depth
    	else:
    		newNodes = []
    		for node in nodeList:
    			if node.left:
    				newNodes.append(node.left)
    			if node.right:
    				newNodes.append(node.right)
    		return self.iterDepth(depth+1, newNodes)
