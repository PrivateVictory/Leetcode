## Maximum Product Subarray

这题是一道很经典的题目，求数组的连续最大积。相类似的有求连续最大和等。很容易想到直接用DP来做。然后就是想怎么DP了。

首先很容易想到直接来dp[i][j]，然后遍历，求i->j的积。然后求其中的Max。
dp[i][j] = dp[i][j-1]*nums[j]. 不过这样TLE了，所以需要再优化。


继续分析，发现这题有个麻烦，就是乘以一个负数。然后再思考，因为只要最大值而不需要把连续的数组给求出来，然后Max的值一般两种，
	max * num(num>0)或者
	min * num(num<0)

对于dp[i]，最大值取决于max.dp[i-1] 和 min.dp[i-1],所以可以得到状态方程：

if nums[i] >0:

max_dp[i] = Math.max(nums[i],max_dp[i-1]*nums[i]);

min_dp[i] = Math.min(nums[i],min_dp[i-1] *nums[i]);

if nums[i] < 0:

max_dp[i] = Math.max(nums[i],min_dp[i-1]*nums[i]);

min_dp[i] = Math.min(nums[i],max_dp[i-1] *nums[i] );


所以我们需要保存每次的max和min。然后判断nun是否大于零。代码如下：

```
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: an integer
     */
    public int maxProduct(int[] nums) {
        int[] max = new int[nums.length];
        int[] min = new int[nums.length];
        
        min[0] = max[0] = nums[0];
        int result = nums[0];
        for (int i = 1; i < nums.length; i++) {
            min[i] = max[i] = nums[i];
            if (nums[i] > 0) {
                max[i] = Math.max(max[i], max[i - 1] * nums[i]);
                min[i] = Math.min(min[i], min[i - 1] * nums[i]);
            } else if (nums[i] < 0) {
                max[i] = Math.max(max[i], min[i - 1] * nums[i]);
                min[i] = Math.min(min[i], max[i - 1] * nums[i]);
            }
            
            result = Math.max(result, max[i]);
        }
        
        return result;
    }
}
```