class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1,1]
        for i in range(2,n+1):
            sum = 0
            for j in range(1,i+1):
                sum += res[j-1]*res[i-j]
            res.append(sum)
        return res[-1]
