__author__ = 'haoxiang'
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = []
        for i in range(len(nums)+1):
            tmp.append(i)
        print sum(tmp) - sum(nums)

Test = Solution()
test = [0,1,3]
Test.missingNumber(test)