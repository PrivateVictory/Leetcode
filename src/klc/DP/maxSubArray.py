"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        iterate through nums, at each element ask whether to include
        it in the current sum or not. Time complexity O(n).
        """
        finalMax= -2**21
        if(len(nums) ==1):
            return nums[0]
        currentMax=-2*31
        for num in nums:
            currentMax=max(currentMax+num, num)
            if (currentMax > finalMax):
                finalMax=max(currentMax, finalMax)
        return finalMax
        
        
