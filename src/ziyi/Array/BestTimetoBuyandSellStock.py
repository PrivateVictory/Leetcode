#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-15 21:19:20
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
        	return 0
        n = len(prices)
        #get everyday's change table
        change_table = [0]*n
        for i in range(1,n):
        	change_table[i] = prices[i] - prices[i-1]
        #find the continues max subarray sum
        maxProfit = change_table[0]
        curProfit = 0
        for i in range(n):
        	curProfit = max(curProfit+change_table[i], change_table[i])
        	maxProfit = max(maxProfit, curProfit)
        if maxProfit < 0:
        	maxProfit = 0
        return maxProfit

def main():
	s = Solution()
	print s.maxProfit([2,1,2,0,1])
	print s.maxProfit([1,4,2])
if __name__ == '__main__':
	main()