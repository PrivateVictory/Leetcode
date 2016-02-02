class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        part = s.strip().split(" ")
        if len(part) == 0:
            return 0
        else:
            return len(part[len(part)-1])
