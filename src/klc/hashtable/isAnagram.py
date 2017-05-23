class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        we sort both lists and compare them, returns true if they are anagrams of each other
        overall complexity is O(n lg n), from calling sorted() in python
        """
        return sorted(t)==sorted(s) 
 

    def isAnagramFast(self, s, t):
     #if both lists are equal length, check if character counts are equal
     #fast solution that is O(n)
        if len(s)==len(t):
            for char in set(s):
                if s.count(char)!=t.count(char):
                    return False
            return True
        else: #clearly not anagrams if s and t have different lengths
            return False
            
    def isAnagram2(self, s, t):
     #create dictionaries for s and t
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2
    
    def isAnagram2(self, s, t):
        dic1, dic2 = [0]*26, [0]*26
        for item in s:
            dic1[ord(item)-ord('a')] += 1
        for item in t:
            dic2[ord(item)-ord('a')] += 1
        return dic1 == dic2
