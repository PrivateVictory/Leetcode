# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # O(logn logn)
        h = self.height(root)
        nodes = 0
        while root:
            if self.height(root.right) == h - 1:
                nodes += 2 ** h  # left half (2 ** h - 1) and the root (1)
                root = root.right
            else:
                nodes += 2 ** (h - 1)
                root = root.left
            h -= 1
        return nodes

    def height(self, root):
        return -1 if not root else 1 + self.height(root.left)
