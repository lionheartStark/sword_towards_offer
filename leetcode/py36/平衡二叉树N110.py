# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def hight(self, root):
        if not root:
            return 0
        else:
            return max(self.hight(root.left), self.hight(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if -1 <= self.hight(root.left) - self.hight(root.right) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
