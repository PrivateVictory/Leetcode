#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-18 01:40:32
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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not root.left or not root.right:
            if root:
                return root.left == root.right
        return self.rec_symmetric(root.left,root.right)
        
    def rec_symmetric(self, p, q):
        if not p or not q:
            return p == q
        return p.val == q.val and \
        self.rec_symmetric(p.left, q.right) and \
        self.rec_symmetric(p.right, q.left)

