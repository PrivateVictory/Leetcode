#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:34:34 2017

@author: Steven
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ans=True
        for c in ransomNote:
            if (c not in magazine):
                ans= False
            elif( c in magazine):
                magazine=magazine.replace(c, "", 1) #Only remove 1 instance! 
        return ans

def main():
    rNote="aa"
    mag="aab"
    s=Solution()
    print(s.canConstruct(rNote, mag))
    
main()