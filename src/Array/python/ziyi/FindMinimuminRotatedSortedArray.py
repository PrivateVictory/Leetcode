#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-17 17:06:58
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : t1174779123.iteye.com

"""
	description:
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
        	return None
        i = 1 
        while i < n and nums[-i] > nums[-i-1]:
        	i += 1
        return nums[-i]
        # lazy mathod
        # return min(nums)
