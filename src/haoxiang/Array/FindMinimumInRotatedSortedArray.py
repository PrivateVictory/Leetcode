class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minNum = 0
        length = len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return None
        isMax = 1 if nums[0]<nums[1] else 2
        for i in range(1,length):
            if isMax == 1 :
                # print minNum
                minNum =nums[0]
                if nums[i]<nums[i-1]:
                    minNum = min(nums[i],nums[0])
                    return minNum
                # minNum = minNum
            elif isMax == 2:
                # print minNum
                minNum = nums[1]
                if nums[i]>nums[i-1]:
                    minNum = min(nums[i-1],minNum)
                    return minNum
        return minNum
Test = Solution()
test = [3,4,5,1,2]
test2 = [5,4,3,1,2]
print Test.findMin(test)
