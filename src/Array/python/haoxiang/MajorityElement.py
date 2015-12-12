class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        newNum = {}
        if n == 1:
            return nums[0]
        for i in range(n):
            if newNum.has_key(nums[i]):
                if newNum[nums[i]] >= (n/2):
                    return nums[i]
                else:
                    newNum[nums[i]] += 1
            else:
                newNum[nums[i]] = 1
