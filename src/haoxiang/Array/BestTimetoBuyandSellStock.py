class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minNum = None
        maxNum = None
        res = 0
        for i in prices:
            if minNum is None or i < minNum:
                minNum = maxNum = i
            elif i>maxNum:
                maxNum = i

            res = max(res,maxNum-minNum)
        return res