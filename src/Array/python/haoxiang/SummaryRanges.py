class Solution:
    def summaryRanges(self,nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        start ,res = 0,[]
        for i in range(1, len(nums)+1):
            if i == len(nums) or nums[i] - nums[i-1] != 1:
                if nums[start]!=nums[i-1]:
                    res.append(str(nums[start])+"->"+str(nums[i-1]))
                else:
                    res.append(str(nums[start]))
                start = i
        print res
        return res
    
Test = Solution()
test = [0,1,2,4,5,7]
Test.summaryRanges(test)