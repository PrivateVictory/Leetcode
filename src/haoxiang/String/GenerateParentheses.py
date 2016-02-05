class Solution(object):
    def __init__(self):
        self.res = []
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.helper('',n,0,0)
        return self.res

    def helper(self,st,max,left,right):
        if right==max:
            self.res.append(st)
        if left<max:
            self.helper(st+'(',max,left+1,right)
        if right<left:
            self.helper(st+')',max,left,right+1)
