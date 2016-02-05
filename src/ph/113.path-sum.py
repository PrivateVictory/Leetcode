# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.flag=False
        self.pathSum(root,sum)
        return self.flag
    def pathSum(self,root,sum):
    	if root==None:
    		return 
    	if root.left==None and root.right==None:
    		if sum==root.val:
    			self.flag=True
    	self.pathSum(root.left,sum-root.val)
    	self.pathSum(root.right,sum-root.val)
