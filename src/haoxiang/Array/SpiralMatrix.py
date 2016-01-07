__author__ = 'haoxiang'
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        x = 0
        y = 0
        res = []
        isLine = True
        while True:
            if isLine:
                if x <= m/2:
                    res.append(matrix[x][y])
                    x+=1
                else :
                    res.append(matrix[x][y])
                    x-=1
            # else :
                # if