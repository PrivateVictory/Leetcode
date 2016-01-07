

class Solution(object):
    # def __init__(self):
    #     self.row=0
    #     self.line=0
    #     self.sunNum=0
    # def minPathSum(self,gird):
    #     self.sumNum = 0
    #     self.row = len(gird)
    #     self.line = len(gird[0])
    #     self.findNext(0,0,gird)
    #     return self.sunNum
    # def findNext(self,i,j,gird):
    #     if i+1 == self.row and j<self.line:
    #         self.findNext(i,j+1,gird)
    #     if j+1 == self.line and i<self.row:
    #         self.findNext(i+1,j,gird)
    #     while i<self.row-1 and j<self.line-1:
    #         self.sunNum+=gird[i][j]
    #         if gird[i+1][j]<gird[i][j+1]:
    #             self.sunNum+=gird[i+1][j]
    #             self.findNext(i+1,j,gird)
    #         elif gird[i+1][j]>gird[i][j+1]:
    #             self.sunNum+=gird[i][j+1]
    #             self.findNext(i,j+1,gird)
    def minPathSum(self,grid):
        row = len(grid)
        line = len(grid[0])
        if row<2 or line <2:
            return sum([sum(i) for i in grid])
        for i in range(row):
            for j in range(line):
                if i ==0 and j ==0:
                    continue
                if i==0:
                    grid[0][j] += grid[0][j-1]
                elif j ==0:
                    grid[i][0] += grid[i-1][0]
                else:
                    grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[row-1][line-1]
        
    # def minPathSum(self,grid):
    #     row = len(grid)
    #     line = len(grid[0])
    #     if row<2 or line <2:
    #         return sum([sum(i) for i in grid])
    #     for i in range(row,0,-1):
    #         for j in range(line,0,-1):
    #             if i ==row-1 and j ==line-1:
    #                 continue
    #             if i==row-1:
    #                 grid[row-1][j] += grid[row-1][j+1]
    #             elif j ==line-1:
    #                 grid[i][line-1] += grid[i+1][line-1]
    #             else:
    #                 grid[i][j] += min(grid[i+1][j],grid[i][j+1])
    #     return grid[0][0]


Test = Solution()
test = [[1,2,5,3],[4,6,2,4],[4,1,5,8]]
print Test.minPathSum(test)
