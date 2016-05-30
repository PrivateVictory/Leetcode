# [213. House Robber II](https://leetcode.com/problems/house-robber-ii/)

> After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

> Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

从题目可知，两个条件：

1. 这是一个环形数组。

2. 相邻的屋子(元素),不能同时被偷。

这道题，是第198题的后续[House Robber](https://leetcode.com/problems/house-robber/)。那么显然，这道题解法与上一道题是一样的，我们可以使用一个以为数组来表示这个圆环数组，只是需要考虑的是最后一个屋子元素与第一个不能同时被偷。

这样的话，第一个元素与最后一个元素不能够同时被考虑到。我们可以把原数组变成两个子数组，一个不包含第一个屋子元素，一个是不包含最后一个屋子元素。

    public int rob(int[] nums) {
        if(nums==null || nums.length<=0) return 0;
        
        if(nums.length==1) return nums[0];
        if(nums.length==2) return Math.max(nums[0], nums[1]);
        
        //以下至少三个点
        int n = nums.length;
        int[] steal = new int[n+1];
        int[] noSteal = new int[n+1];
        int max = 0;
        //最后一个与第一个也不能同时偷
        //当第一个元素被偷
        for(int i=2;i<=n;i++){
            steal[i] = Math.max(noSteal[i-1]+nums[i-1],steal[i-1] );
            noSteal[i] = Math.max(steal[i-1], noSteal[i-1]);
        }
        //max = steal[n] + nums[0];
        max = steal[n];
        
        //当第一个元素没有被偷时
        for(int i=1;i<n;i++){
            steal[i] = Math.max(noSteal[i-1]+nums[i-1],steal[i-1] );
            noSteal[i] = Math.max(steal[i-1], noSteal[i-1]);
        }
        return Math.max(max, steal[n-1]);
    }