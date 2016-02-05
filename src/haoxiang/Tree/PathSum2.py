# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        tmp = []
        if root is None:
            return self.res
        self.findPath(root,tmp,sum)
        return self.res

    def findPath(self,root,tmp,sum):

        sum -= root.val
        tmp.append(root.val)
        if not (root.left and root.right):
            if sum == 0:
                self.res.append(tmp)
                return
        if root.left is not None:self.findPath(root.left,tmp)
        if root.right is not None:self.findPath(root.right,tmp)
