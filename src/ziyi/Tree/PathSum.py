#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-10 00:10:06
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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
        	return False
        if root.left:
        	root.left.val += root.val
        if root.right:
        	root.right.val += root.val
        if not root.left and not root.right and root.val == sum:
        	return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


    





