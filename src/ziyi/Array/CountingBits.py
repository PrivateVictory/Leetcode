#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-28 23:38:03
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com
'''
	description: O(n*logn)
'''

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dividers = [1]
        bits = []
        for i in range(num+1):
        	# print 'i : ',i,'div : ',dividers
        	t_bits = 0
        	for d in dividers:
        		if (d & i) == d:
        			t_bits += 1
        			# print 't_bits:',t_bits
        	if i == (dividers[-1] << 1 ):
        		dividers.append(dividers[-1] << 1 )
        		t_bits += 1
        		# print 'add 2',dividers
        	bits.append(t_bits)
        return bits

def main():
	s = Solution()
	print s.countBits(5)
	print s.countBits(64)
	


if __name__ == '__main__':
	main()







