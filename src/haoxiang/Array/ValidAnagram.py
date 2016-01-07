

class Solution(object):
    def isAnagram(self, s, t):
           s = "".join((lambda x:(x.sort(),x)[1])(list(s)))
           t = "".join((lambda x:(x.sort(),x)[1])(list(t)))
           return t == s
