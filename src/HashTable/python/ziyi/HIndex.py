#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-17 23:53:45
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
    description: solved in O(n) time complexity
'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        # traverse fitst to get map 
        table = [0]*(n+1)
        for citation in citations:
            table[n-min(citation, n)] += 1
        # traverse twice to get better map
        for i in range(1,n+1):
            table[i] += table[i-1]
        # traverse third to find the h_index
        for i, count in enumerate(table):
            if count >= n-i:
                return n-i
        return 0

def main():
    s = Solution()
    print s.hIndex([])
    print s.hIndex([0])
    print s.hIndex([1])
    print s.hIndex([100])
    print s.hIndex([99,100])

if __name__ == '__main__':
    main()



