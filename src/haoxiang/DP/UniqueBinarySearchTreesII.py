# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.genTree(1,n)
    def genTree(self,s,e):
        tmp = []
        if s>e:
            tmp.append(None)
            return tmp
        for i in range(s,e+1):
            l = self.genTree(s,i-1)
            r= self.genTree(i+1,e)
            for j in l:
                for k in r:
                    node = TreeNode(i)
                    node.left = j
                    node.right = k
                    tmp.append(node)
        return tmp

        
