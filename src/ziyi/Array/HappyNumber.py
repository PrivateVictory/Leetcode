#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-14 21:02:00
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
    description: 
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mid_results = []
        temp = n
        while 1:
            result = 0
            while temp:
                result += (temp%10)**2
                temp /= 10
            temp = result
            if result == 1:
                return True
            elif result in mid_results:
                return False
            else:
                mid_results.append(result)
                
def main():
    s = Solution()
    print s.isHappy(19)
    print s.isHappy(20)
if __name__ == '__main__':
    main()
    
