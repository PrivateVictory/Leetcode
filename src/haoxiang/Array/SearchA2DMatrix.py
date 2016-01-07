class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        line = len(matrix)
        row = len(matrix[0])
        for i in range(line):
            if target <= matrix[i][row-1]:
                for j in range(row):
                    if matrix[i][j] == target:
                        return True
        return False