

class Solution(object):
    def maxSubArray(self, nums):
        length = len(nums)
        currSum = 0
        maxSum = nums[0]
        for j in range(length):
        #     if nums[i]>currSum:
        #         currSum = nums[i]
        #     else:
        #         currSum+=nums[i]
        #     #maxSum = (maxSum > currSum) ? maxSum : currSum
        #     if maxSum < currSum:
        #         maxSum = currSum
            currSum = max(nums[j], currSum + nums[j])
            print "currSum:"+str(currSum)
            maxSum = max(maxSum, currSum)
            print "max:"+str(maxSum)
        return maxSum
Test = Solution()
test = [1, -2, 3, 10, -4, 7, 2, -5]
print Test.maxSubArray(test)
