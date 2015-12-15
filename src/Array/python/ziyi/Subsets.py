#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-14 22:59:48
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description: solved by recursion
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.rec_subsets(nums)
    
    def rec_subsets(self,nums):
        #return condition
        if len(nums) == 0:
            return [[]]
        #start recursion
        without_head = self.rec_subsets(nums[1:])
        with_head = [([nums[0]] + x) for x in without_head]
        return with_head + without_head

def main():
    s = Solution()
    print s.subsets([1,2,3])
if __name__ == '__main__':
    main()