class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: res[res[int]]
        """
        res = [0]*numRows
        if numRows == 0:
            res =[]
            return res
        if numRows == 1:
            res = [[1]]
            return res
        else :
            res[0] = [1]
            res[1] = [1,1]
            for i in range(2,numRows):
                res[i] = [0]*(i+1)
                res[i][0] = res[i][i] = 1
                for j in range(1,i):
                    res[i][j] = res[i-1][j-1]+res[i-1][j]
            print res
            return res

Test = Solution()
Test.generate(5)