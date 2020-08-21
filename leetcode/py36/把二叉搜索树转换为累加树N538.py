# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.right_sum = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        else:

            self.convertBST(root.right)
            self.right_sum += root.val
            root = self.right_sum
            self.convertBST(root.left)

            return root
