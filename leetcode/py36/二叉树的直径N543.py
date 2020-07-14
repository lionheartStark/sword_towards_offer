# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def count_deep(self, root):
        if not root:
            return 0
        else:
            left_deep = self.count_deep(root.left)
            right_deep = self.count_deep(root.right)
            self.res = max(self.res, left_deep + right_deep + 1)
            return 1 + max(left_deep, right_deep)
        pass

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.res = 1

        if not root:
            return 0
        else:
            self.count_deep(root)

        return self.res-1

