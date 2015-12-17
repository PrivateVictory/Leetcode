__author__ = 'lenovo'
# -*- coding: utf-8 -*-
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        num = sorted(num)
        i,result = 0, set()
        while i < len(num) - 2:
            j, k = i + 1, len(num) - 1
            while j < k:
                if num[i] + num[j] + num[k] == 0:
                    result.add((num[i], num[j],num[k]))
                    j += 1
                elif num[i] + num[j] + num[k] > 0:
                    k -= 1
                else:
                    j += 1
            i+=1
        print  [list(t) for t in result]
test = Solution()
lists = [-1 ,0 ,1, 2, -1, -4]
test.threeSum(lists)