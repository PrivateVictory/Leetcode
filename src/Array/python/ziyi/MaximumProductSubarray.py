#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-15 09:47:27
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p_max, n_max = 1, 1
        result = nums[0]
        for num in nums:
        	if num < 0:
        		p_max, n_max = n_max, p_max
    		p_max = max(p_max * num, num)
    		n_max = min(n_max * num, num)
    		result = max(result, p_max)
        return result

def main():
	s = Solution()
	print s.maxProduct([2,3,-2,4])
if __name__ == '__main__':
	main()
