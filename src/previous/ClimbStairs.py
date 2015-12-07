__author__ = 'lenovo'

# -*- coding: utf-8 -*-
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

斐波那契
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        prefirst = 1
        presecond = 2
        result = 0
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        else :
            for i in range(2,n):
                result = prefirst+presecond
                prefirst = presecond
                presecond = result
            return result


