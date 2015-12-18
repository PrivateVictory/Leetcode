#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-17 19:12:33
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : t1174779123.iteye.com

"""
	description:
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res  = []
        for i in range(n):
        	if i > 0 and nums[i] == nums[i-1]:
        		continue
        	j, k = i+1, n-1
        	target = -nums[i]
        	while j < k:
        		if nums[j] + nums[k] == target:
        			res.append([nums[i], nums[j], nums[k]])
        			while j < k and nums[j+1] == nums[j]:
        				j += 1
        			while j < k and nums[k-1] == nums[k]:
        				k -= 1
        			j += 1 
        			k -= 1
        		elif nums[j] + nums[k] < target:
        			j += 1 
        		else:
        			k -= 1
        return res

def main():
	s = Solution()
	print s.threeSum([-1, 0, 1, 2, -1, -4])
	print s.threeSum([0,0,0])
if __name__ == '__main__':
	main()






        	


        	
    
