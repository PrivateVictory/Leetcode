# -*- coding: utf-8 -*-
__author__ = 'lenovo'
def myAtoi(strs):
        num =0
        lens = len(strs)
        if lens > 1:
            for i in range(0,lens):
                num += int(strs[i])*10**(lens-1)
                lens -=1
        print(num)

myAtoi("36894234")