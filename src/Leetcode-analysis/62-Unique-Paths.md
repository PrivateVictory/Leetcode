# [62. Unique Paths](https://leetcode.com/problems/unique-paths/)

> A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

> The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

> How many possible unique paths are there?

知道，矩阵中某一元素若果是从左上角到右下角的路径经过的一点，那么只有从该元素上方或者左方才能到达该元素所在位置，所以，到达该元素所有的路径是，到达该元素左边相邻元素的路径数和到达该元素上方相邻元素的路径数之和。如此，问题便精简成，求解从左上角达到该元素左边相邻元素的路径数，以及从左上角到达该元素上方相邻元素的路径数，依次类推。

	public int uniquePaths(int m, int n) {
        if(m<=0 || n<=0) return 0;
        int[][] dp = new int[m][n];
        for(int i=0;i<m;i++){
        	dp[i][0] = 1;
        }
        for(int i=0;i<n;i++){
        	dp[0][i] = 1;
        }
        for(int i=1;i<m;i++){
        	for(int j=1;j<n;j++){
        		dp[i][j] = dp[i-1][j]+dp[i][j-1];
        	}
        }
        return dp[m-1][n-1];
    }

