"""
Given an array of integers and an integer k, find out whether
there are two distinct indices i and j in the array such that nums[i] = nums[j] 
and the absolute difference between i and j is at most k.

Very similar to solving "Contains Duplicate" without the restriction of being nearby.
Just changed the logic in line 20 to check whether the difference between the index of the existing
v in dictionary is <= k. If not, there may still be a nearby duplicate value, so update the current value's index.
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d ={}
        for i, v in enumerate(nums):
            if v not in d:
                d[v]=i
            else:
                if (abs(d[v]-i)<=k):
                    return True
                else:
                    d[v]=i
        return False
                
        
