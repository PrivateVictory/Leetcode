#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-06 19:33:37
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        quotient = n
        result = ''
        while quotient:
        	remainder = quotient % 26
        	quotient = quotient / 26
        	if remainder:
        		result = chr(remainder-1+ord('A')) + result
        	else:
        		result = 'Z' + result
        		quotient -= 1
        return result

def main():
	s = Solution()
	print s.convertToTitle(7)
	print s.convertToTitle(26)
	print s.convertToTitle(30)
	print s.convertToTitle(26*26*2)
	print s.convertToTitle(26*26)
	print s.convertToTitle(26*26*2+1)
	print s.convertToTitle(26*26*26)
	print s.convertToTitle(26*26*26+1)
if __name__ == '__main__':
	main()

