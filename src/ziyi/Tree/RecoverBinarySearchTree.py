#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-18 13:11:00
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
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.pre_node = None
        self.first_node = None
        self.second_node = None
        # dfs
        self.dfs(root)
        #exchange value
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val

    # dfs: from the min to max 
    def dfs(self, root):
    	if not root:
    		return
    	self.dfs(root.left)

    	if self.pre_node and root.val < self.pre_node.val:
    		if not self.first_node:
    			self.first_node = self.pre_node
    			self.second_node =  root # consider that two nodes may be next to each other
    		else:
    			self.second_node = root
    	
    	self.pre_node = root
    	
    	self.dfs(root.right)


