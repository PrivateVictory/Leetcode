"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.
How many possible unique paths are there?
Note: m and n will be at most 100.
The time and space complexity are both O(n*m). The recurrence relation is that numberUniquePaths(i, j) depends on two previous possibilities,
numberUniquePaths(i-1, j) and numberUniquePaths(i, j-1). We use a two dimensional array (python list) for memoization.
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        paths = [1] * m
        for i in range(m):
            paths[i] = [1] * n
        for i in range(1,m):
            for j in range(1,n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[-1][-1]
        
