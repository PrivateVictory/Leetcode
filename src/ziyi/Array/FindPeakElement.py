#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-17 17:21:08
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : t1174779123.iteye.com

"""
    description: solved by dichotomy
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.n = len(nums)
        if self.n == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        self.nums = nums
        return self.findHalf(0,self.n-1)

    def findHalf(self, start, stop):
        i = start + (stop-start) / 2
        #not at the first or the last element
        if i != 0 and i != self.n-1:
            # \ shape, find left
            if self.nums[i-1] > self.nums[i] > self.nums[i+1]:
                return self.findHalf(start, i)
            # / shape, find right
            elif self.nums[i-1] < self.nums[i] < self.nums[i+1]:
                return self.findHalf(i+1, stop)
            # \/ shape, find left(or right or both)
            elif self.nums[i] < self.nums[i-1] and self.nums[i] < self.nums[i+1]:
                return self.findHalf(start, i)
            # /\ shape, return 
            elif self.nums[i] > self.nums[i-1] and self.nums[i] > self.nums[i+1]:
                print 'i = ',i,'self.nums[i] = ',self.nums[i]
                return i    
        else:
            print 'i = ',i,'self.nums[i] = ',self.nums[i]
            return i 
def main():
    s = Solution()
    print s.findPeakElement([1,2])
    # s.findPeakElement([1,2,3,4,5,6])
    # s.findPeakElement([1,7,3,4,5,6])
    # s.findPeakElement([1,2,3,8,5,6])
    # s.findPeakElement([8,2,3,4,5,6])
    # s.findPeakElement([6,5,7,3,2,1])
    # s.findPeakElement([4,5,7,3,2,1,0,8])
    # s.findPeakElement([1,3,5,7,9,1])

if __name__ == '__main__':
    main()


