#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-15 11:51:38
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        for i in range(1,n):
    		for j in range(i+1):
    			if j is 0:
    				triangle[i][j] += triangle[i-1][j]
    			elif j == i:
    				triangle[i][j] += triangle[i-1][j-1]
    			else:
    				triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        #print_tri(triangle)
        return min(triangle[-1])

def print_tri(tri):
	for i in range(len(tri)):
		for j in range(i+1):
			print tri[i][j],'\t',
		print ''

def main():
	s = Solution()

	print s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
if __name__ == '__main__':
	main()