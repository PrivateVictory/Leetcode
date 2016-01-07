#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-05 13:01:03
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = num
        while result >= 10:
        	temp = result
        	result = 0
        	while temp:
        		result += temp % 10
        		temp /= 10
        return result
def main():
	s = Solution()
	print s.addDigits(38)
	print s.addDigits(10)

if __name__ == '__main__':
	main()
