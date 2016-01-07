__author__ = 'lenovo'

# -*- coding: utf-8 -*-
import string

class Solution:
    # @param s, a string
    # @print an integer
    def numDecodings(self, s):
        if not s:
            return 0

        if s[-1] == '0':
            right = 0
            right_right = 1
        else:
            right=right_right=1

        for i in range(len(s)-2, -1, -1):
            if s[i] == '0':
                right, right_right = 0, right
            else:
                # choose one to decode
                count_one = right
                # choose two to decode
                count_two = right_right if 0 < int(s[i:i+2]) <= 26 else 0
                right, right_right = count_one+count_two, right
        print right


test = Solution()
test.numDecodings('12130')
