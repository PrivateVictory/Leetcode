# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def countNodes(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root==None:
#         	return 0
#         hl=0
#         hr=0
#         rl=root
#         rr=root
#         while rl:
#         	hl=hl+1
#         	rl=rl.left
#         while rr:
#         	hr=hr+1
#         	rr=rr.right
#         if hl==hr:
#         	return pow(2,hl)-1
#         return 1+self.countNodes(root.left)+self.countNodes(root.right)

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.re=0
        self.count(root)
        return self.re
    def count(self,root):
     	if root!=None:
        	self.re=self.re+1
           	self.count(root.left)
           	self.count(root.right)


s=Solution()
print s.countNodes(TreeNode(1))
