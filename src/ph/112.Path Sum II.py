# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.result=[]
        self.path=[]
        self.pathGet(root,sum)
        return self.result
    def pathGet(self,root,sum):
    	if root==None:
    		return 
    	self.path.append(root.val)
    	if root.left==None and root.right==None and sum==root.val:
    		self.result.append(self.path[:])
    	self.pathGet(root.left,sum-root.val)
    	self.pathGet(root.right,sum-root.val)
    	self.path.pop()

