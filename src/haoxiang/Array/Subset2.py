__author__ = 'haoxiang'
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res={}
        new_res = []
        res[0]=[[],[nums[0]]]

        for i in range(1,len(nums)):
            res[i]=res[i-1]+[x+[nums[i]] for x in res[i-1]]
        for j in range(len(res[len(nums)-1])):
            if res[len(nums)-1][j] not in new_res:
                new_res.append(res[len(nums)-1][j])
        return new_res

Test = Solution()
test = [1,2,2]
print Test.subsetsWithDup(test)