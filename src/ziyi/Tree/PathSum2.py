#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-10 22:04:27
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
    		return []
        self.res = []
        root.path = [root.val]
        root.path_val = root.val
    	self.recPathSum(root, sum)
    	return self.res
    def recPathSum(self,node,sum):
    	if node.left:
    		node.left.path = node.path + [node.left.val]
    		node.left.path_val = node.path_val + node.left.val
    		self.recPathSum(node.left, sum)
    	if node.right:
    		node.right.path = node.path + [node.right.val]
    		node.right.path_val = node.path_val + node.right.val
    		self.recPathSum(node.right, sum)

    	if not node.left and not node.right and node.path_val == sum:
    		self.res.append(node.path)




