class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.findRes(n)
    def findRes(self,num):
        num = str(num)
        sum = 0
        res=""
        for i in num:
            j = int(i)
            sum +=j^2
            res=res+str(j)
        if sum == 1:
            print "yes"
            return True
        else:
            self.findRes(int(res))
Test = Solution()
Test.findRes(19)
