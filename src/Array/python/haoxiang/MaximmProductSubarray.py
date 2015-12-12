class Solution(object):
    def maxProduct(self, nums):
        # currSum = 1
        maxSum,minSum= nums[0],nums[0]
        res=nums[0]
        if len(nums) == 1:
            return nums[0]
        for i in range(1,len(nums)):
            if nums[i] > 0:
                maxSum = max(nums[i],maxSum*nums[i])
                minSum = min(nums[i],minSum*nums[i])
            else:
                tmplast = maxSum
                maxSum = max(minSum*nums[i],nums[i])
                minSum = min(tmplast*nums[i],nums[i])
            res = max(res,maxSum)
        return res
Test = Solution()
test = [2,3,-2,4]
print Test.maxProduct(test)
