# [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

> Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

从题意看，我们要从矩阵的左上角走到右下角，移动的方向只有往下或者是往右，如果矩阵中某一元素是从左上角到右下角的路径中经过的一个位置，那必然是从其上方或者左方到达该位置的。

这是一个很明显的动态规划问题。在grid里面的每一个元素都是与其上方相邻元素以及左方相邻元素有关(当然，在边界上面的元素特殊情况特殊分析，比如grid[0][0]没有相关的元素，而矩阵最左边的元素只与它的上方的相邻元素相关，最上面的一行元素只与它的左边相邻元素相关)。并且是相关元素与该元素之和。


	public int minPathSum(int[][] grid) {
        if(grid==null || grid.length<=0) return 0;
        int m = grid.length;
        int n = grid[0].length;
        int[][] dp = new int[m][n];
        dp[0][0] = grid[0][0];
        for(int i=1;i<m;i++){
        	dp[i][0] = dp[i-1][0]+grid[i][0];
        }
        for(int i=1;i<n;i++){
        	dp[0][i] = dp[0][i-1]+grid[0][i];
        }
        for(int i=1;i<m;i++){
        	for(int j=1;j<n;j++){
        		dp[i][j] = Math.min(dp[i][j-1]+grid[i][j], dp[i-1][j]+grid[i][j]);
        	}
        }
        return dp[m-1][n-1];
    }



