# [55. Jump Game](https://leetcode.com/problems/jump-game/)

> Given an array of non-negative integers, you are initially positioned at the first index of the array.Each element in the array represents your maximum jump length at that position.

> Determine if you are able to reach the last index.

> For example:

> A = [2,3,1,1,4], return true.

> A = [3,2,1,0,4], return false.

这道题很明显的有子问题的特征。假设我们有一个有着n个元素的数组nums，第n-1个元素可以跳跃的最大距离(从第0个位置开始算起)是nums[n-1]+n-1，而在0到n-1的这段子数组里面可以跳跃的最大距离是nums[n-1]+n-1与他的0到n-2的子数组的最大可跳跃距离的较大值，即是说：

> cache[i] = Math.max(cache[i-1], nums[i]+i);

其中，cache[i]表示0到i这段子数组的可跳跃的最大距离。只要cache[i]大于n即是说明，可以跳跃到最后的第n-1位置。而如果'cache[i]==i'，即是说明最多只能跳到第i个位置，然后无法再继续前进了。

	public boolean canJump(int[] nums) {
        if(nums==null || nums.length<=0) return false;
        if(nums.length==1) return true;
        if(nums[0]==0) return false;
        int len = nums.length;
        //可跳跃距离在 nums[pos]以内
        //应该是计算出前几的可跳跃最长距离。只要该距离大于len即可
        int[] cache = new int[len];
        cache[0] = nums[0];
        for(int i=1;i<len;i++){
        	//cache[i-1]  nums[i]+pos
        	cache[i] = Math.max(cache[i-1], nums[i]+i);
        	//如果cache[i] == i
        	if(cache[i]==i) return false;
        	if(cache[i]>=len-1) return true;
        }
        return false;
    }