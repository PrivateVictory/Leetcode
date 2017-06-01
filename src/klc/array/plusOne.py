class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result=0
        n=len(digits)-1
        for i in digits:
           result+= i*10**n
           n-=1
        result+=1
        return [int(i) for i in str(result)]
