__author__ = 'haoxiang'
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        sumNum = triangle[0][0]
        # if len(triangle)<3:
        #
        line = len(triangle)
        for  i in range(1,line):
            for j in range(len(triangle[i])):
                if j>0 and j<len(triangle[i])-1:
                    triangle[i][j] += min(triangle[i-1][j],triangle[i-1][j-1])
                if j == 0 or j == len(triangle[i])-1:
                    triangle[i][j]+= triangle[i-1][j]
        reslist = sorted(triangle[len(triangle)-1])
        return reslist[0]
