#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-17 21:42:56
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : t1174779123.iteye.com

"""
    description:
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cur_longth = 0
        max_longth = 0
        start = stop = 0
        table = {}
        for i in range(n):
            stop += 1
            ch = s[i]
            if not table.has_key(ch):
                table[ch] = i
            else:
                for j in range(start, table[ch]):
                    table.pop(s[j])
                start = table[ch] + 1
                table[ch] = i
            cur_longth = stop - start
            max_longth = max(cur_longth, max_longth)
        return max_longth
def main():
    s = Solution()
    print s.lengthOfLongestSubstring('abcabcbb')
    print s.lengthOfLongestSubstring('bbbbbb')
    print s.lengthOfLongestSubstring('aab')

if __name__ == '__main__':
    main()





