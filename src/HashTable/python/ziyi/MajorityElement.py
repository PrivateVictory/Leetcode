#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-17 14:37:54
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : t1174779123.iteye.com

"""
	description:
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        distribution = {}
        for num in nums:
        	if num not in distribution.keys():
        		distribution[num] = 1
        	else:
        		distribution[num] += 1
        		if distribution[num] > n/2:
        			return num

def main():
    s = Solution()
    print s.majorityElement([1,1,2,2,2])
    
if __name__ == '__main__':
	main()
