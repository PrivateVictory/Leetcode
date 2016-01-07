class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        l = len(citations)
        res = 0
        for i in range(l):
            if citations[i] < l-1-i:
                res = citations[i]
            elif citations[i] >= l-i:
                res = max(res, l-i)
                break
        return res
         
