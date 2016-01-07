class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return list(self.combine(sorted(candidates), target))
    def combine(self,candidate,target):
        for i,item in enumerate(candidate):
            if target > item:
                for it in self.combine(candidate[i:],target-item):
                    yield [item]+it
            elif target == item:
                yield [item]

Test = Solution()
test = [2,3,6,7]
test2=[1,2]
print Test.combinationSum(test,2)