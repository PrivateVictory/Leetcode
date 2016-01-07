__author__ = 'lenovo'

class Solution:
    def compareVersions(self,version1,version2):
        ch1 = version1.split('.')
        ch2 = version2.split('.')
        i = 0
        j = 0
        res = 0
        while i < len(ch1) and j < len(ch2):
            num1 = int(ch1[i])
            num2 = int(ch2[j])
            if num1 > num2:
                res = 1
                return res
            elif num1 < num2:
                res = -1
                return res
            else:
                i += 1
                j += 1
        if i < len(ch1) and j == len(ch2):
            if int(ch1[i]) != 0:
                res = 1
        if i == len(ch1) and j < len(ch2):
            if int(ch2[j]) != 0:
                res = -1
        if i == len(ch1) and j == len(ch2):
            num1 = int(ch1[i-1])
            num2 = int(ch2[j-1])
            if num1 > num2:
                res = 1
            elif num1 < num2:
                res = -1
        return res

test = Solution()
test.compareVersions(3,4.6)