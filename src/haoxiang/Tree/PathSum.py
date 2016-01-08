# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        res = sum - root.val
        if not (res or root.left or root.right):
            return True
        return self.hasPathSum(root.left,res) or self.hasPathSum(root.right,res)
