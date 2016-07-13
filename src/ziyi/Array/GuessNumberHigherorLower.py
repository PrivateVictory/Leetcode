#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-13 15:08:01
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : t1174779123.iteye.com

"""
	description:
"""

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
        	return None
        if n == 1:
        	return 1 
        if n > 1:
        	return self.recuGuessNumber(1,n+1)
    def recuGuessNumber(self, start, stop):
    	guessNum = (start + stop) / 2
    	result = guess(guessNum)
    	if not result:
    		return guessNum 
    	elif result == 1:
    		return self.recuGuessNumber(guessNum, stop)
    	elif result == -1:
    		return self.recuGuessNumber(start,guessNum)

def main():
	s = Solution()
	print s.guessNumber(100)
if __name__ == '__main__':
	main()
