class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        #without using reverse slice, which is
        return s[::-1]. But it's faster to use reverse slicing.
        """
        result=[]
        n=len(s)
        count=1
        for i in range(len(s)):
            result.append(s[n-count])
            count +=1
        result = ''.join(result)
        return result
 
