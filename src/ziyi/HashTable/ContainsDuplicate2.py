#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-07 00:30:52
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        table = {}
        for i,num in enumerate(nums):
        	if table.has_key(num) and i - table[num] <= k:
        		return True	
	        else:
	        	table[num] = i
        return False

def main():
	s = Solution()
	print s.containsNearbyDuplicate([1,2,1],3)


