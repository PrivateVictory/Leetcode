#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-17 14:25:41
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : t1174779123.iteye.com

"""
	description: sum all positive changes
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
        	return 0
        return sum([x for x in [(prices[i]-prices[i-1]) for i in range(1,n)] if x > 0])

def main():
	s = Solution()
	print s.maxProfit([5,6,5,7,9,6,11,10,8])

if __name__ == '__main__':
	main()










