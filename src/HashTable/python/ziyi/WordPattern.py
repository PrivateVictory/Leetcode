#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-18 01:31:27
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = str.split(' ')
        table = {}
        for ch, s in zip(pattern, strs):
        	if not table.has_key(ch):
        		table[ch] = s
        	elif table[ch] != s:
        		return False
        return True

def main():
	s = Solution()
	print s.wordPattern('abba','dog cat cat dog')
	print s.wordPattern('abba','cat dog cat dog')
if __name__ == '__main__':
	main()


