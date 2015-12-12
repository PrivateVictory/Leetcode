__author__ = 'haoxiang'
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # sort = sorted(nums)

        if sum(nums) < s or not nums:
            return 0
        length = len(nums)
        start =0
        end =0
        res =length
        sums =0
        while start<length:
            sums+=nums[start]
            start+=1
            if sums>=s:
                while sums-nums[end]>=s:
                    sums-=nums[end]
                    end+=1
                res = min(start-end,res)
        print res




Test = Solution()
test = [1,2,3,4,5]
Test.minSubArrayLen(11,test)