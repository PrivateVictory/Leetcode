

class Solution(object):
    def uniquePaths(self, m, n):
        sumNum = 0
        tmp =1
        if m<2 or n<2:
            return 1
        if m==2 and n==2:
            return 2
        for i in range(1,m):
            tmp = tmp+n-2
            sumNum+=tmp
        return sumNum
