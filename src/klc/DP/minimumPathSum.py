"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes 
the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
The cost at (i,j) in the grid is obviously the value at (i,j) plus the previous cost. There are two possible
previous squares and we take the minimum of the two possibilities. Time complexity O(nm), space complexity O(nm),
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i][j]+ min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
