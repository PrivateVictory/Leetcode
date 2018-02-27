class Solution:
    # @param x, an integer
    # @return an integer
    def mySqrt(self, x):
        if x == 0:
            return 0
        low, high, ans, =1, x, 1
        
        while low != high - 1:
            mid = low + (high-low)/2
            if mid * mid > x:
                high = mid
            elif mid * mid < x:
                ans = mid
                low = mid
            else:
                return mid
        return mid
