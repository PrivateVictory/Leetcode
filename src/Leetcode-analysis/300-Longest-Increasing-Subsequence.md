# [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

> Given an unsorted array of integers, find the length of longest increasing subsequence.

> For example,given [10, 9, 2, 5, 3, 7, 101, 18],

> The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

一句话，这个动态规划的关键是，当前的数组元素的最长递增序列是之前小于当前元素的数组元素的最长递增序列+1，并取其中的最大值。


	public int lengthOfLIS(int[] nums) {
        if(nums==null || nums.length<=0) return 0;
        int len = nums.length;
        int[] dp = new int[len];
        for(int i=0;i<len;i++){
        	dp[i] = 1;
        }
        for(int i=1;i<len;i++){
        	for(int j=i-1;j>=0;j--){
        		if(nums[i]>nums[j]) {
        			dp[i] = Math.max(dp[i], dp[j]+1);
        		}
        	}
        }
        int max = 0;
        for(int i=0;i<len;i++){
        	max = Math.max(max, dp[i]);
        }
        return max;
    }



