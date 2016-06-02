# [221. Maximal Square](https://leetcode.com/problems/maximal-square/)

> Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

> For example, given the following matrix:

	1 0 1 0 0
	1 0 1 1 1
	1 1 1 1 1
	1 0 0 1 0

> Return 4.

因为要求的是，该矩阵中最大的方阵的面积，而我们要确保求得到的是一个方阵(正方形)，需要迭代遍历该矩阵，其中每一个元素matrix[i][j]就与matrix[i-1][j-1]、matrix[i-1][j]、matrix[i][j-1]有关。

	public int maximalSquare(char[][] matrix) {
        if(matrix==null || matrix.length<=0) return 0;
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] dp = new int[m+1][n+1];
        for(int i=1;i<=m;i++){
        	for(int j=1;j<=n;j++){
        		if(matrix[i-1][j-1]=='0') dp[i][j] = 0;
        		else{
        			dp[i][j] = Math.min(dp[i-1][j],Math.min(dp[i][j-1], dp[i-1][j-1]))+1;
        		}
        	}
        }
        int max = 0;
        for(int i=0;i<=m;i++){
        	for(int j=0;j<=n;j++){
        		max = Math.max(max, dp[i][j]);
        	}
        }
        return (int) Math.pow(max, 2);
    }



