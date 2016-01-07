#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-13 15:29:05
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s = [0]*26
        count_t = [0]*26
        for ch in s:
        	count_s[ord(ch)-ord('a')] += 1
        for ch in t:
        	count_t[ord(ch)- ord('a')] += 1

        for i in range(26):
        	if count_s[i] != count_t[i]:
        		return False
        return True
