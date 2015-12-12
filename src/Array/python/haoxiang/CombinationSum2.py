__author__ = 'haoxiang'
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = list(self.combine(sorted(candidates), target))
        resu = []
        for i in res:
            if i not in resu:
                resu.append(i)
        return resu
    def combine(self,candidate,target):
        for i,item in enumerate(candidate):
            if target > item:
                for it in self.combine(candidate[i+1:],target-item):
                    yield [item]+it
            elif target == item:
                yield [item]