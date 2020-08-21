# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:  # Definition for a binary tree node.
        if root == None:
            return None
        else:
            tmp = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
            root.right = tmp

        return root
