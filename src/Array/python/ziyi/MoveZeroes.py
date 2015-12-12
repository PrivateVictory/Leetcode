#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-12 19:39:31
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description:
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        print 'nums = ',nums
        #find zero positions
        zero_pos = []
        for i,each_num in enumerate(nums):
        	if not each_num:
        		zero_pos.append(i)
        zero_pos.append(len(nums))
        #move nums
        for i in range(1,len(zero_pos)):
    		for j in range(zero_pos[i-1]+1,zero_pos[i]):
    			nums[j], nums[j-i] = nums[j-i], nums[j]

def main():
	s = Solution()
	s.moveZeroes([1,0,2,0,0,3])
	s.moveZeroes([1,0,2,3,0,0,4,5,0])

if __name__ == '__main__':
	main()






