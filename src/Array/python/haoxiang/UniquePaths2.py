

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        # line = len(obstacleGrid)
        # row = len(obstacleGrid[0])
        #
        # res = [0]*(row+1)
        # for i in range(1,line):
        #     for j in range(1,row):
        #         res[j] = res[j]+res[j-1]  if obstacleGrid[i-1][j-1]==0 else 0
        # return res[line-1]
        # use DP
        sumNum = 0
        line = len(obstacleGrid)
        row = len(obstacleGrid[0])
        res= [[0 for x in range(row)] for x in range(line)]

        # if (m<2 or n<2):
        #     return 1
        # if (m==n==2):
        #     return 2
        for x in range(line):
            res[x][0] = 1
        for y in range(row):
            res[0][y] = 1
        for i in range(1,line):
            for j in range(1,row):
                res[i][j] = res[i-1][j]+res[i][j-1] if obstacleGrid[i-1][j-1]==0 else 0
        return res[line-1][row-1]

Test = Solution()
