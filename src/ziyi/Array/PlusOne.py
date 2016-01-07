#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-15 11:21:02
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #plus one on the last digit
        digits[-1] += 1
        #then carry
        for i in range(1,len(digits)+1):
        	if not i == len(digits):
        		#carry to higher digit
        		if digits[-i] == 10:
        			digits[-i] = 0
        			digits[-i-1] += 1
        		else:
        			break
        	elif digits[-i] == 10:#create new digit
        		digits[-i] = 0
        		digits.insert(0,1)
        return digits

def main():
	s = Solution()
	print s.plusOne([1,9,9])
	print s.plusOne([9,9,9])
if __name__ == '__main__':
		main()	
