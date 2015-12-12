
class Solution(object):
        def moveZeroes(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            num = 0
            if not nums:
                 return
            # else :
            #     while step<len(nums):
            #         if nums[step] == 0:
            #             num+=1
            #             nums.remove(0)
            #         step+=1
            #     for i in range(num):
            #         nums.append(0)
            #     return nums
            # for i in range(len(nums)):
            #     if nums[i] is 0:
            #         num+=1
            # for j in range(num):
            #     nums.remove(0)
            # for k in range(num):
            #     nums.append(0)
            # return nums
            else:
                for i in range(len(nums)):
                    if nums[i] !=0:
                        nums[num],nums[i] = nums[i],nums[num]
                        num+=1
                return nums

Test = Solution()
test = [0, 1, 0, 3, 12]
print Test.moveZeroes(test)
