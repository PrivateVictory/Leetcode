class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        res = 0
        minNum = maxNum = prices[0]

        for i in range(1,len(prices)):
            # if minNum is None:
            #     minNum = maxNum =prices[i]
            if prices[i] > maxNum:
                maxNum = prices[i]
            else:
                res= res+(maxNum-minNum)
                minNum = maxNum = prices[i]
        res+=(maxNum-minNum)
        return res
            