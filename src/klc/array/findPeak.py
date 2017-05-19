class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallNumber=(-2**31)-1
        prevNumber= nextNumber = smallNumber
        if (len(nums)<=1):
            return 0
        #elif(len(nums)==2): unnecessary after loop below handles the peak element in beginning or end case
            #return nums.index(max(nums))
        for i in range(len(nums)):
            nextNumber=(nums[i+1] if (i+1<len(nums)) else smallNumber) #set to next element in nums only if i+1 exists
            if(nums[i]> prevNumber and nums[i] > nextNumber):
               return i
            prevNumber=nums[i]
           
