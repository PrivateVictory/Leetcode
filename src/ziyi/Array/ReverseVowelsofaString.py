#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-27 23:42:01
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com
'''
	description: 1 find the vowels and save others
				 2 save pos and ch
				 3 pop vowels to complate the str
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l < 2:
        	return s
        vowels = ['a','e','i','o','u','A','E','I','O','U'] 
        vowel_pos = []
        list_s = []
        list_vowels = []
        for i, ch in enumerate(s):
        	if ch in vowels:
        		list_s.append('\0')
        		vowel_pos.append(i)
        		list_vowels.append(ch)
        	else:
        		list_s.append(ch)
        for pos in vowel_pos:
        	list_s[pos] = list_vowels.pop()
        return ''.join(list_s)

def main():
	s = Solution()
	print s.reverseVowels('hello')
	print s.reverseVowels('leetcode')
if __name__ == '__main__':
	main()


