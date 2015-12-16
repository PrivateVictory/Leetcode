#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-15 22:12:56
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #consider empty set
        if len(nums) == 0:
        	return False
        #quick sort and compare neighbours
        nums.sort()
        for i in range(1,len(nums)):
        	if nums[i] == nums[i-1]:
        		return True
        return False


def main():
	s = Solution()
	print s.containsDuplicate([1,2,3])
	print s.containsDuplicate([1,2,3,3])
	print 
if __name__ == '__main__':
	main()

