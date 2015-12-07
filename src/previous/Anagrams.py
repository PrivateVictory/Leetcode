__author__ = 'lenovo'
# -*- coding: utf-8 -*-
'''
Given an array(数组) of strings, return all groups of strings that are anagrams(回文构词法).

Note: All inputs(投入) will be in lower-case(小写字母的).
'''
from collections import defaultdict
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        groups = defaultdict(list)
        for word in strs:
            groups[''.join(sorted(word))].append(word)

        answer = []
        for group in groups.values():
            if len(group) > 1:
                answer.extend(group)
        print answer
test =Solution()
lists = ['asdfdsa','sdafas','hjklkjh','asd','das']
test.anagrams(lists)