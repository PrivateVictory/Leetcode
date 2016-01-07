__author__ = 'lenovo'
'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
'''
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        lenth = len(nums)
        print nums[lenth-k:lenth]
        print nums[0:lenth-k]
        nums[:]=nums[lenth-k:lenth]+nums[0:lenth-k]

if __name__ == '__main__':
    list = [1,2,3,4,5,6,7]
    test = Solution()
    test.rotate(list,3)
