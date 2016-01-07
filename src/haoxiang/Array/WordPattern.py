class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        part = str.split(" ")
        print part
        lens = len(part)
        res = {}
        result = ""
        if lens is not len(pattern):
            return False
        for i in range(lens):
            if res.has_key(part[i]):
                if pattern[i] in result:
                    result+=pattern[i]
                else:
                    return False
            else:
                if pattern[i] in result:
                    return False
                else:
                    tmp = [i]
                    res[part[i]] = tmp
                    result+=pattern[i]
        print result
        if pattern == result:
            return True
        else:
            return False
Test = Solution()
pattern =  "abba"
string ="a b b c"

print Test.wordPattern(pattern,string)
