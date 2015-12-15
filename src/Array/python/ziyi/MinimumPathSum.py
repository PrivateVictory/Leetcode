#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-13 09:51:28
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com

'''
	description: solved with DP
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #DP: save the min to the every grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) == (0, 0):
                    continue
                elif i is 0:
                    grid[i][j] += grid[i][j-1]
                elif j is 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]

   #low efficiency mothod
   #      self.m,self.n = len(grid),len(grid[0])
   #      self.grid = grid5
   #      self.minPathSum = -1
   #      self.recuMinPathSum(cur_raw = 0, cur_col = 0, mid_result = grid[0][0])
   #  	return self.minPathSum
   #  #recursive mathod
   #  def recuMinPathSum(self, cur_raw, cur_col, mid_result):
   #  	if cur_raw == self.m-1 and cur_col == self.n-1:
   #  		if self.minPathSum == -1:
   #  			self.minPathSum = mid_result
   #  		else:
   #  			self.minPathSum = min(self.minPathSum, mid_result)	

   #  	elif cur_raw < self.m-1 and cur_col < self.n-1:
			# mid_result_down = mid_result + self.grid[cur_raw+1][cur_col]
			# mid_result_right = mid_result + self.grid[cur_raw][cur_col+1]
			# return self.recuMinPathSum(cur_raw+1, cur_col, mid_result_down),\
			# self.recuMinPathSum(cur_raw, cur_col+1, mid_result_right)
   #  	elif cur_raw == self.m-1 and cur_col < self.n-1:
   #  		mid_result_right = mid_result + self.grid[cur_raw][cur_col+1]
   #  		return self.recuMinPathSum(cur_raw, cur_col+1, mid_result_right)
   #  	elif cur_raw < self.m-1 and cur_col == self.n-1:
   #  		mid_result_down = mid_result + self.grid[cur_raw+1][cur_col]
   #  		return self.recuMinPathSum(cur_raw+1, cur_col, mid_result_down)

def main():
	s = Solution()
	g = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	print s.minPathSum(g)
if __name__ == '__main__':
	main()


