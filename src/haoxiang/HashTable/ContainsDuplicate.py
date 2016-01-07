class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        newList = {}
        for i in nums:
            if not newList.has_key(i):
                newList[i]=1
            else:
                return True
        return False