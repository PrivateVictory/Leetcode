package com.cyw.leetcode;

/**
 * https://leetcode.com/problems/minimum-path-sum/
 * You can only move either down or right at any point in time.
 * @author cyw
 *
 */
public class MinimumPathSumProblem64 {
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
	public static void main(String[] args) {

	}

}
