#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-26 23:11:05
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
'''
	description: 
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l < 2:
        	return s

        return s[::-1]
        

def main():
	s = Solution()
	test_s = ''
	print s.reverseString('hello')
if __name__ == '__main__':
	main()


