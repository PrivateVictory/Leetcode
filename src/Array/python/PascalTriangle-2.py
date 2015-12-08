__author__ = 'haoxiang'
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [0]*(rowIndex+1)
        if rowIndex == 0:
            res =[[1]]
            return res[0]
        if rowIndex == 1:
            res = [[1],[1,1]]
            return res[1]
        else :
            res[0] = [1]
            res[1] = [1,1]
            for i in range(2,rowIndex+1):
                res[i] = [0]*(i+1)
                res[i][0] = res[i][i] = 1
                for j in range(1,i):
                    res[i][j] = res[i-1][j-1]+res[i-1][j]
            print res[rowIndex]
            return res[rowIndex]

Test = Solution()
Test.getRow(5)