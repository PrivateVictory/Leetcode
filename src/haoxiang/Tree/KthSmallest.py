# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
     def kthSmallest(self, root, k):
        count = self.get_nodes(root.left)
        while count + 1 != k:
            if count + 1 < k:
                root = root.right
                k = k - count - 1
            else:
                root = root.left
            count = self.get_nodes(root.left)
        return root.val

    def get_nodes(self, root):
        if not root:
            return 0
        return 1 + self.get_nodes(root.left) + self.get_nodes(root.right)
