

class Solution(object):
    def uniquePaths(self, m, n):
        # use DP
        # sumNum = 0
        # res= [[0 for x in range(n)] for x in range(m)]
        #
        # if (m<2 or n<2):
        #     return 1
        # if (m==n==2):
        #     return 2
        # for x in range(m):
        #     res[x][0] = 1
        # for y in range(n):
        #     res[0][y] = 1
        # for i in range(1,m):
        #     for j in range(1,n):
        #         res[i][j] = res[i-1][j]+res[i][j-1]
        # return res[m-1][n-1]


        #use Math
        sum1 = 1
        sum2 =1
        sum3 =1
        for i in range(1,m+n-1):
            sum1*=i
        for j in range(1,m):
            sum2*=j
        for k in range(1,n):
            sum3*=k
        return sum1/(sum2*sum3)