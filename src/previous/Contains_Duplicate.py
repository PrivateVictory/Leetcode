__author__ = 'haoxiang'

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return not (len(nums)==len(set(nums)))