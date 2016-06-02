# [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)

> Follow up for "Unique Paths":

> Now consider if some obstacles are added to the grids. How many unique paths would there be?

> An obstacle and empty space is marked as 1 and 0 respectively in the grid.

> For example,

> There is one obstacle in the middle of a 3x3 grid as illustrated below.

	[
	  [0,0,0],
	  [0,1,0],
	  [0,0,0]
	]

> The total number of unique paths is 2.

思路是跟62题是一样的，只是，如果该位置元素为1，是障碍物，则表示此路不通，则该位置的路径数应该是0.

	/**
	 * Now consider if some obstacles are added to the grids. 
	 * @param obstacleGrid
	 * @return
	 */
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if(obstacleGrid==null || obstacleGrid.length<=0) return 0;
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[][] dp = new int[m][n];
        if(obstacleGrid[0][0]==1) dp[0][0] = 0;
        else dp[0][0] = 1;
        for(int i=1;i<m;i++){
        	if(obstacleGrid[i][0]==1) dp[i][0] = 0;
        	else dp[i][0] = dp[i-1][0];
        }
        for(int i=1;i<n;i++){
        	if(obstacleGrid[0][i]==1) dp[0][i] = 0;
        	else dp[0][i] = dp[0][i-1];
        }
        for(int i=1;i<m;i++){
        	for(int j=1;j<n;j++){
        		if(obstacleGrid[i][j]==1) dp[i][j]=0;
        		else{
        			dp[i][j] = dp[i-1][j]+dp[i][j-1];
        		}
        	}
        }
        return dp[m-1][n-1];
    }


