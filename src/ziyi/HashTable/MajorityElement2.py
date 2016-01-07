#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-17 14:49:27
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : t1174779123.iteye.com

"""
	description: Moore's Voting Algorithm: True gold does not fear fire
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n < 2:
        	return nums
        elif n == 2:
        	if nums[0] == nums[1]:
        		return [nums[0]]
        	else:
        		return nums
        count = [0,0]
        candidates = [0,1]#make them different is better
        #traverse first to find the candidates 
        for num in nums:
        	if num == candidates[0]:
        		count[0] += 1
        	elif num == candidates[1]:
        		count[1] += 1
        	elif count[0] == 0:
        		candidates[0] = num
        		count[0] += 1
        	elif count[1] == 0:
        		candidates[1] = num
        		count[1] += 1 
        	else:
        		count[0] -= 1 
        		count[1] -= 1
       	#traverse twice to find the real majority element
       	count = [0,0]
       	result = []
       	for num in nums:
       		if num == candidates[0]:
       			count[0] += 1 
       		elif num == candidates[1]:
       			count[1] += 1
       	for i in range(2):
       		if count[i] > n/3:
       			result.append(candidates[i])
       	return result

def main():
	s = Solution()
	print s.majorityElement([1])
	print s.majorityElement([1,2])
	print s.majorityElement([2,2])
	print s.majorityElement([1,2,3,3])
	print s.majorityElement([1,2,2,3,3])

if __name__ == '__main__':
	main()

