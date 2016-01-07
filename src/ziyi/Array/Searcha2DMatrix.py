#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-16 11:13:23
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : t1174779123.iteye.com

"""
	description:
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0 or target < matrix[0][0]:
        	return False

        for i in range(m):
        	if matrix[i][n-1] > target:
        		for j in range(n):
        			if matrix[i][j] == target:
        				return True
        	elif matrix[i][n-1] == target:
        		return True
        return False

def main():
	s = Solution()
	a = [[1,2,3],[4,5,6],[7,8,9]]
	print s.searchMatrix(a,4)
	print s.searchMatrix(a,10)
	print s.searchMatrix(a,0)


if __name__ == '__main__':
	main()



