__author__ = 'lenovo'
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,

Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    '''
    自己第一次的做法 O（n^2）
    '''
    def trap(self, A):
        big_a = []
        big_b = []
        sum = 0
        B = A[::-1]
        for i in range(0,len(A)-1):
            if i == 0:
                big_a.append(A[0])
            else:
                temp = A[0:i]
                big_a.append(max(temp))
        for j in range(0,len(B)-1):
            if j == 0:
                big_b.append(B[0])
            else:
                temp = B[0:j]
                big_b.append(max(temp))
        print(big_a)
        print(big_b)
        for k in range(0,len(A)-1):
            if A[k] < min(big_a[k],big_b[k]):
                sum+=(min(big_a[k],big_b[k])-A[k])
        print sum
        return sum

    '''
    别人的做法 O(1)
    '''
    def trap_2(self, arr):
        left = right = water = 0
        i, j = 0, len(arr)-1
        while i <= j:
            left, right = max(left, arr[i]), max(right, arr[j])
            while i <= j and arr[i] <= left <= right:
                water += left - arr[i]
                i += 1
            while i <= j and arr[j] <= right <= left:
                water += right - arr[j]
                j -= 1
        return water
    '''
    别人的做法 O(0)
    '''
    def trap_2(self, arr):
        height, left, right, water = [], 0, 0, 0
        for i in arr:
            left = max(left, i)
            height.append(left)
        height.reverse()
        for n, i in enumerate(reversed(arr)):
            right = max(right, i)
            water += min(height[n], right) - i
        return water
if __name__ == '__main__':
    list = [2,0,1]
    # for i in range(0,100):
    #     i = random.randint(1,100)
    #     list.append(i)
    test = Solution()
    test.trap(list)