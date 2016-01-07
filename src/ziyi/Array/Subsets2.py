#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-15 20:10:25
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
    description: solved in an ugle way....
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        subsets =  self.rec_subsets(nums)
        result = []
        for each_set in subsets:
            if each_set not in result:
                result.append(each_set)
        return result

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
    print s.subsetsWithDup([1,2,3,4])
    print s.subsetsWithDup([1,2,2,3,3,4])
if __name__ == '__main__':
    main()

#------------wrong answer---------------
# class Solution(object):
#     def subsetsWithDup(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         n = len(nums)
#         nums.sort()
#         subsets = [[]]
#         for i in range(n):
#           if i is 0:
#               for num in nums:
#                   temp = [num]
#                   if temp not in subsets:
#                       subsets.append(temp)
#           else:
#               for j in range(n-i):
#                   for k in range(j+i,n):
#                       temp = nums[j:j+i] + [nums[k]]
#                       if temp not in subsets:
#                           subsets.append(temp)
#         return subsets