class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.sort(nums)
        indexList=self.findSum(nums,target)
        return indexList
    def sort(nums):
    	for i in range(len(nums)):
    		for j in range(i,len(nums)):
    			if nums[j]<nums[i]:
    				nums[i],nums[j]=nums[j],nums[i]


    def findsum(start,end,nums,target):
    	while nums[start]+nums[end]<target:
    		start=start+1
    	

