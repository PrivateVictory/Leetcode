#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-13 14:45:30
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
    description:
'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        DP_grid = [[0]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                #if meets obstacle
                if obstacleGrid[i][j]:
                    continue #keep DP_grid[i][j] zero
                elif (i,j) == (0,0):
                    DP_grid[i][j] = 1
                elif i is 0:#on up side
                    DP_grid[i][j] = DP_grid[i][j-1]
                elif j is 0:#on left side
                    DP_grid[i][j] = DP_grid[i-1][j]
                else:#inside grid
                    DP_grid[i][j] = DP_grid[i-1][j] + DP_grid[i][j-1]
        print_grid(DP_grid)
        return DP_grid[-1][-1]

def print_grid(grid):
    for x,R in enumerate(grid):
        for y,_ in enumerate(R):
            print _,'\t',
        print ''
    print ''

def main():
    s = Solution()
    print s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
if __name__ == '__main__':
    main()



