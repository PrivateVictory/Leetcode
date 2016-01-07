__author__ = 'haoxiang'

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        sum =0
        temp = 0
        if n < 1:
            return 0
        for i in range(0,n):
            for j in range(0,i):
                if j%i == 1:
                    temp += 1
                if temp != 0 :
                    sum +=1
                    temp = 0
        print sum
        return sum

test = Solution()
test.countPrimes(10)