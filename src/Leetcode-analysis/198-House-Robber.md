# [198. House Robber](https://leetcode.com/problems/house-robber/)

> You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
> Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

从题目可知，两个条件：

1. 这是一个一维数组。

2. 相邻的屋子(元素),不能同时被偷。

首先，很明显的知道可以使用分治法、用递归来解决这个问题。

假设，小偷偷了第0个屋子，那么相邻的第1个屋子，今晚就不能偷了，而剩下的屋子，又变成一个新的一维数组，这时候同样的需要考虑是否偷第2个屋子。而每一个屋子，都有两种可能，即是被偷和没有被偷。

基于以上的分析，我们可以写一个递归，对这一个一维数组进行递归求解，保存得到最大的偷到的钱财的值。

	public int rob(int[] nums) {
      if(nums==null || nums.length<=0) return 0;
      return robDC(nums, 0);
    }
    /*
    	递归过程，参数是这一排的屋子(一个数组)，以及一个整数，表示从第start个屋子开始偷。
    */
    public int robDC(int[] nums, int start){
        if(nums==null || nums.length<=0 || start<0) return 0;
        if(start==nums.length-1) return nums[start];
        if(start==nums.length-2) 
        	return Math.max(nums[start], robDC(nums, start+1));
        //取得最大值，第一个参数是表示第start个屋子被偷了，第二个表示该屋子没有被偷。
        return Math.max(nums[start]+robDC(nums, start+2), robDC(nums, start+1));
    }

以上，递归能够很好的解决问题，但是这只能对于数量较少的屋子，对于拥有较少元素的一维数组有效，但是对于数量巨大的一维数组中，时间消耗很大程度上都消耗在了计算上面，效率较低。

那么，如何有效的提高性能呢？有人就发现，其实在进行递归的时候，有着大量的重复计算，比如在计算robDC(nums, start)与计算robDC(nums, start+2)的时候，就多次重复计算了robDC(nums, start+2)。类似的重复计算还有很多，尤其是在数组元素过于巨大的时候，多余的计算带来的大量的时间成本是我们承受不起的。这时候，为了解决这个重复计算的缺陷，有人就想到了是否可以把计算结果给保存起来，当下次需要计算的时候，直接就从缓存中得到计算结果，从而省略了计算的过程，时间成本降低。这也是经典的以空间换时间的思想。

以上，我们便可以发现，这不正是动态规划的特点吗？递归表示该问题有子问题，有最优的子问题。重复计算，说明了该问题有重叠的子问题，计算重复。所以，这个题目，我们可以使用DP来解决。

	public int rob(int[] nums) {
        if(nums==null || nums.length<=0) return 0;
        
        int n = nums.length;
        int[] steal = new int[n+1];
        int[] noSteal = new int[n+1];
        steal[0] = 0;
        noSteal[0] = 0;
        //表示数组的大小。得到缓存表的结果
        for(int i=1;i<=n;i++){
        	//如果小偷偷第i-1个屋子
        	steal[i] = Math.max(noSteal[i-1]+nums[i-1],steal[i-1] );
        	//如果小偷不偷第i-1个屋子
        	noSteal[i] = Math.max(steal[i-1], noSteal[i-1]);
        }
        return steal[n];
    }
