class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos = 0
        lens = len(nums) - 1
        res = [-1, -1]

        while pos <= lens:
            start = end = (pos+lens)/2
            if nums[start] > target:
                lens = start-1
            elif nums[start] < target:
                pos = start+1
            else:
                while pos < start:
                    mid = (pos+start)/2
                    if nums[mid] is not target:
                        pos = mid + 1
                    else:
                        start = mid
                while lens > end:
                    mid = (lens+end)/2+1
                    if nums[mid] is not target:
                        lens = mid -1
                    else:
                        end = mid
                return [start,end]
        return res

Test = Solution()
s = [5, 7, 7, 8, 8, 10]
s2 = [2,2]
print Test.searchRange(s2,2)
