# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.res = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        s = ""
        if root is None:
            return self.res
        self.findPath(root,s)
        return self.res
    def findPath(self,root,string):
        if root.left is None and root.right is None:
            self.res.append(string+str(root.val))
            return
        string +=str(root.val)+"->"
        if root.left is not None :
            self.findPath(root.left,string)
        if root.right is not None:
            self.findPath(root.right,string)
        return
