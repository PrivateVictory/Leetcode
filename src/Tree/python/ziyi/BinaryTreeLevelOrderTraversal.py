#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-05 13:54:45
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
        	return []
        else:
        	return self.iterOrder([root], [])
    def iterOrder(self, nodeList, result):
    	if nodeList == []:
    		return result
    	else:
    		cur_level = []
    		new_nodes = []
    		for node in nodeList:
    			cur_level.append(node.val)
    			if node.left:
    				new_nodes.append(node.left)
    			if node.right:
    				new_nodes.append(node.right)
    		result.append(cur_level)
    		return self.iterOrder(new_nodes, result)


