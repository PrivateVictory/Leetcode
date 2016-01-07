#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-18 01:00:55
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.recTraversal(root, res)
        return res

    def recTraversal(self,node,res):
    	if not node:
    		return 
    	if node.left == node.right == None:
    		res.append(node.val)
    		return
    	self.recTraversal(node.left,res)
    	res.append(node.val)
    	self.recTraversal(node.right,res)








