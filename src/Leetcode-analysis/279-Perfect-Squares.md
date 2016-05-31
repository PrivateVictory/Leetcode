# [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)

> Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

> For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

这又是一个动态规划的问题。首先，我们知道已知n，这样可以求得1-n之间的perfect square numbers(完全平方数)都有哪些。比如n为26时候，perfect square numbers为1到(int) (Math.sqrt(n))。注意此时(int) (Math.sqrt(n))是向下取整的。

> dp[i] = Math.min(dp[i], dp[(int) (i-Math.pow(j, 2))]+1);

关键是这个公式了。和为n的最小数目的perfect square numbers是由n减去小于n的perfect square numbers得到的数所对应的和为其的最少perfect square numbers数目+1.并且相互比较，取其中的最小值。依此递归下去。当然，我们不用递归。这次还是使用的动态规划来求解吧。

	public int numSquares(int n) {
        if(n<=0) return 0;
        int[] dp = new int[n+1];
        dp[0] = 0;
        dp[1] = 1;
        for(int i=2;i<=n;i++){
        	dp[i] = Integer.MAX_VALUE;
        }
        for(int i=2;i<=n;i++){
        	int maxSq = (int) (Math.sqrt(i));
        	for(int j=maxSq;j>0;j--){
        		dp[i] = Math.min(dp[i], dp[(int) (i-Math.pow(j, 2))]+1);
        	}
        }
        return dp[n];
    }


