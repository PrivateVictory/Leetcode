class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 0
        res = []
        if len(s) is 0:
            return 0
        if len(s) is 1:
            return 1
        for i in range(1,len(s)):
            if s[i] is not s[start]:
                end = i
                print "start:"+str(start)+" end:"+str(end)+">>>"
            else:
                print "start:"+str(start)+" end:"+str(end)
                res.append(len(s[start:end+1]))
                start = end =i
        res.append(len(s[start:end+1]))
        res.sort()
        print res
        return res[len(res)-1]
                
Test = Solution()
test = "bdb"
print Test.lengthOfLongestSubstring(test)