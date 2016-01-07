#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-14 18:07:55
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for num in nums:
        	ret ^=num 
        return ret

def main():
	s = Solution()
	print s.singleNumber([1,2,3,2,1])
if __name__ == '__main__':
	main()
