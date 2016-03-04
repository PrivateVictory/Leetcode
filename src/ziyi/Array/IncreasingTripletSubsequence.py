#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-27 10:40:08
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : t1174779123.iteye.com

"""
    description: 通过不断保存最小的中间值，寻找比中间值大的数来完成任务
            注意：不需要考虑最小值在中间值之后的情况，因为中间值存在就意味着
            判断middle条件不要写not middle。因为middle可能是0
"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3:
            return False
        minimun, middle = nums[0], None
        for i in [x+1 for x in range(n-1)]:
            if nums[i] < minimun:
                minimun = nums[i]
                print 'update min: min=%d, middle='%(minimun),middle
            if nums[i] > minimun:
                if middle == None or middle > nums[i]:
                    middle = nums[i]
                    print 'update middle: min=%d, middle=%d'%(minimun,middle)
            if middle != None and nums[i] > middle:
                return True
        return False

        
def main():
    s = Solution()
    print s.increasingTriplet([1,2,3,4,5])
    print s.increasingTriplet([1,1,3,4,5])
    print s.increasingTriplet([5,4,3,2,1])
    print s.increasingTriplet([5,4,1,2,3])
    print s.increasingTriplet([2,5,5,4,1,5])
    print s.increasingTriplet([1,0,0,0,-1,0,0,0,10000])

if __name__ == '__main__':
    main()
