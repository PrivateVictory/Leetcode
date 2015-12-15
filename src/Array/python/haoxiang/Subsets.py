__author__ = 'haoxiang'

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res={}
        res[0]=[[],[nums[0]]]

        for i in range(1,len(nums)):
            res[i]=res[i-1]+[x+[nums[i]] for x in res[i-1]]
        return res[len(nums)-1]

Test = Solution()
test = [1,2,3]
print Test.subsets(test)