#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-06 20:34:34
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i, ch in enumerate(reversed(s)):
        	result += (ord(ch)-ord('A')+1) * 26**i
        return result

def main():
	s = Solution()
	print s.titleToNumber('Z')
	print s.titleToNumber('YZ')

if __name__ == '__main__':
	main()