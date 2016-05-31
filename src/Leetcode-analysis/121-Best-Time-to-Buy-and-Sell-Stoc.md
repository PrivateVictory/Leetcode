# [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

> Say you have an array for which the ith element is the price of a given stock on day i.

> If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

注意，这次的股票交易至多只有一次交易。所以，很简单，遍历prices数组，只要求出一个i之前的局部最小值，并得到每一位数组元素对应的与局部最小值的差值，得到最大的差值即可。

	public int maxProfit(int[] prices) {
        if(prices==null || prices.length<=1) return 0;
        int len = prices.length;
        int min = prices[0];
        int maxPro = 0;
        for(int i=1;i<len;i++){
        	min = Math.min(min,prices[i]);
        	maxPro = Math.max(maxPro, prices[i]-min);
        }
        return maxPro;
    }





