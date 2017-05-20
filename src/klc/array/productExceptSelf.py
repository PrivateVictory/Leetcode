'''
Given an array of n integers where n > 1, nums, return an array output such that output[i] is
equal to the product of all the elements of nums except nums[i].
Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        productSoFar=1
        
        for i in range(len(nums)): #first pass fills output partially with product left of index i
            output.append(productSoFar)
            productSoFar *= nums[i]
        productSoFar=1 #reset it before going backwards through nums    
        
        for i in range(len(nums)-1, -1, -1): #now fill output with product of elements right of index i
            output[i]*= productSoFar
            productSoFar *= nums[i]
        return output
