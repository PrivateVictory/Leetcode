class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newRes = {}
        res = []
        n = len(nums)
        for i in nums:
            if newRes.has_key(i):
                newRes[i]+=1
            else:
                newRes[i]=1
        for key in newRes:
            if newRes[key]>n/3:
                res.append(key)
        return res