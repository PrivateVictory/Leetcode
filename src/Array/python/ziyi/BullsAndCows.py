#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-14 20:15:15
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        sec_left = [0]*10
        bull_list = []
        bulls = 0
        cows = 0
        #find bulls first
        for i in range(len(secret)):
        	num_s, num_g = secret[i], guess[i]
        	if num_g == num_s:
        		bulls += 1
        		bull_list.append(i)
        	else:
        		sec_left[ord(num_s)-ord('0')] += 1
        #then find cows
        for i in [x for x in range(len(secret)) if x not in bull_list]:
        	num_g = ord(guess[i]) - ord('0')
        	if sec_left[num_g]:
        		cows += 1
        		sec_left[num_g] -= 1
        return '%dA%dB'%(bulls,cows)

def main():
	s = Solution()
	print s.getHint('1123', '1132')
	print s.getHint('1123', '0111')
if __name__ == '__main__':
	main()

