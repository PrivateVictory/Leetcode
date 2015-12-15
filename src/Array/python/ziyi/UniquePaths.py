#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-13 14:37:40
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = 1
        for i in range(n-1):
        	result *= m + n - 2 - i
        for i in range(n-1):
        	result /= i
        return result
        

