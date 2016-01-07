#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-13 11:25:23
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        cur_sum = 0
        
        for i in range(len(nums)):
            #cur_sum + nums[i] < nums[i], shows the sum before less than zero, abandon it.
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum

def main():
	s = Solution()
	print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

if __name__ == '__main__':
		main()	


