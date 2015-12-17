class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while ((r-l)>1):
            m = (l+r)/2
            if nums[m]>nums[m+1]:
                r = m
            else:
                l = m+1
        return l if (nums[l]>nums[r]) else r