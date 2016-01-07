__author__ = 'lenovo'
# -*- coding: utf-8 -*-
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        lens = len(A)
        p = 1
        for i in range(1,lens):
            if A[i] != A[i-1]:
                A[p] = A[i]
                p+=1
        return p

