"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""


class Solution(object):
 def maxProduct(self, nums):
    maximum=big=small=nums[0]
    for n in nums[1:]:
        big, small=max(n, n*big, n*small), min(n, n*big, n*small)
        maximum=max(maximum, big)
    return maximum 
