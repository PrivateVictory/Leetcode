#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-03 23:34:35
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.rec_invertTree(root)
        return root

    def rec_invertTree(self, node):
     	if node:
        	node.left, node.right = node.right, node.left
        	self.rec_invertTree(node.left)
        	self.rec_invertTree(node.right)