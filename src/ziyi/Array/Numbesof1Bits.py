#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-04 23:44:16
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
'''
	description:
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
        	print 'n = ',n
        	if n%2:
        		res += 1
        	n /= 2
        return res

def main():
	s = Solution()
	print s.hammingWeight(11)
if __name__ == '__main__':
	main()