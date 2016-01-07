class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        line = len(matrix)
        row = len(matrix[0])
        x = 0
        y = 0
        for i in range(line):
            if target is matrix[i][row-1]:
                return True
            elif target < matrix[i][row-1]:
                x = i
                break
            else:
                x = line-1
        for j in range(row):
            if target is matrix[line-1][j]:

                return True
            elif target < matrix[line-1][j]:
                y = j
                break
            else :
                y = row-1
        for k in range(x,line):
            for l in range(y,row):
                if matrix[k][l] is target:
                    print str(matrix[k][l])+">>>"
                    return True
        return False

Test = Solution()
test = [[48,65,70,113,133,163,170,216,298,389],[89,169,215,222,250,348,379,426,469,554],[178,202,253,294,367,392,428,434,499,651],[257,276,284,332,380,470,516,561,657,698],[275,331,391,432,500,595,602,673,758,783],[357,365,412,450,556,642,690,752,801,887],[359,451,534,609,654,662,693,766,803,964],[390,484,614,669,684,711,767,804,857,1055],[400,515,683,732,812,834,880,930,1012,1130],[480,538,695,751,864,939,966,1027,1089,1224]]

print Test.searchMatrix(test,642)